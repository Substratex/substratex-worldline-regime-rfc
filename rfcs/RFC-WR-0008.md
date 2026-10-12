# RFC-WR-0008 — Lead-Time and Prospective Validity

**Status:** Draft  
**Target:** WRS 1.0  
**Namespace:** `urn:substratex:worldline-regime:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


Formal lead-time is `Δt = t_f - t_star`.

It is computable only when `t_star` is confirmed, `t_f` is supplied/observed and qualified, coordinates are compatible, and the declared method permits comparison.

If `t_f` is unavailable, formal `Δt` SHALL be `not_computable`. A warning interval may remain open as `open_watch`.

A prospective warning claim at coordinate `t` MUST use only evidence available at or before `t`. A retrospective precursor must not be relabeled as prospective warning without prospective detector evaluation.


---
Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
