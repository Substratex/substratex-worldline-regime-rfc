# RFC-WR-0007 — Temporal Markers and Coordinates

**Status:** Draft  
**Target:** WRS 1.0  
**Namespace:** `urn:substratex:worldline-regime:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


WRS 1.0 defines:

- `t_aw` — first qualified weakening;
- `t_candidate` — candidate boundary;
- `t_star` — confirmed boundary / Basin Exit;
- `t_f` — qualified observable failure;
- `t_recovery_candidate`;
- `t_recovery`.

Every marker carries marker type, coordinate, coordinate system, evidence horizon, status, method/version, evidence references, and qualification state.

`t_star` does not create `t_f`. A confirmed boundary does not establish failure.

A generic run origin (`T0`) MUST NOT substitute for a scientific transition or failure marker.


---
Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
