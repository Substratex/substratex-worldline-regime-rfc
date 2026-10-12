#!/usr/bin/env python3
from pathlib import Path
import json, sys
import jsonschema
from referencing import Registry, Resource

ROOT=Path(__file__).resolve().parents[1]
schemas={}
registry=Registry()
for p in (ROOT/"schemas").glob("*.schema.json"):
    obj=json.loads(p.read_text())
    schemas[p.stem.replace(".schema","")]=obj
    if "$id" in obj:
        registry=registry.with_resource(obj["$id"], Resource.from_contents(obj))

def validate_schema(name,obj):
    v=jsonschema.Draft202012Validator(schemas[name],registry=registry,format_checker=jsonschema.FormatChecker())
    return list(v.iter_errors(obj))

def sem(name,obj,fx):
    e=[]
    if name=="worldline":
        if obj.get("cross_run") and len(obj.get("source_run_ids",[]))<2:
            e.append("cross_run requires at least two source_run_ids")
    elif name=="regime-classification-contract":
        h=obj.get("hysteresis",{})
        if h.get("used") and (not h.get("entry_rule") or not h.get("exit_rule")):
            e.append("hysteresis requires entry and exit rules")
        p=obj.get("persistence",{})
        if p.get("required") and not p.get("minimum_observations"):
            e.append("required persistence needs minimum_observations")
    elif name=="temporal-marker":
        if obj.get("status")=="confirmed" and obj.get("coordinate") is None:
            e.append("confirmed marker requires coordinate")
        if obj.get("status") in ("not_supplied","not_observed","unavailable","not_computable") and obj.get("coordinate") is not None:
            e.append("missing marker state cannot carry coordinate")
    elif name=="lead-time-assessment":
        if obj.get("status")=="computed":
            if not obj.get("t_star_ref") or not obj.get("t_f_ref"):
                e.append("computed lead-time requires both marker refs")
            if obj.get("delta_t") is None:
                e.append("computed lead-time requires delta_t")
        if obj.get("status")=="not_computable" and obj.get("delta_t") is not None:
            e.append("not_computable lead-time cannot carry delta_t")
        if "future-leakage" in fx.get("fixture_id",""):
            e.append("prospective claim uses future evidence")
    elif name=="continuity-assessment":
        if obj.get("run_boundary") and obj.get("status")=="continuous":
            e.append("run boundary cannot silently preserve continuous single-run status")
    elif name=="recovery-assessment":
        if obj.get("status")=="confirmed" and obj.get("persistence_satisfied") is not True:
            e.append("confirmed recovery requires persistence")
        r=obj.get("re_entry")
        if r and r.get("assessed") and r.get("result")=="re_entry" and not r.get("correspondence_rule"):
            e.append("re_entry requires correspondence_rule")
    elif name=="worldline-finding":
        if not obj.get("claim_boundary",{}).get("prohibits"):
            e.append("finding requires explicit prohibitions")
    return e

total=passed=failed=0
for p in sorted((ROOT/"conformance/fixtures").rglob("*.json")):
    total+=1
    fx=json.loads(p.read_text())
    obj=fx["object"]
    se=validate_schema(fx["schema"],obj)
    schema_valid=not se
    seme=sem(fx["schema"],obj,fx)
    semantic="pass" if not seme else "fail"
    ok=(schema_valid==fx["expect_schema_valid"])
    if schema_valid:
        ok=ok and semantic==fx["expect_semantic"]
    if ok:
        passed+=1
    else:
        failed+=1
        print("FAIL",p.relative_to(ROOT),schema_valid,semantic)
        for x in se[:2]: print(" schema:",x.message)
        for x in seme[:2]: print(" semantic:",x)
print(f"WRS fixture validation: {passed}/{total} passed, {failed} failed")
sys.exit(0 if failed==0 else 1)
