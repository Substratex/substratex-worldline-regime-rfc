# RFC-WR-0004 — Regime Classification and Hysteresis

**Status:** Draft  
**Target:** WRS 1.0  
**Namespace:** `urn:substratex:worldline-regime:1.0:`  
**Originator:** Arjay Asadi  
**Publisher:** SubstrateX®


Every authoritative regime assignment SHALL resolve to a versioned Regime Classification Contract declaring required signals, eligible evidence horizon, thresholds/decision rules, persistence, hysteresis where used, missingness behavior, candidate/confirmed behavior, uncertainty semantics, permitted regimes, forbidden interpretations, and method/version identity.

If required evidence is unavailable, the classifier SHALL emit a typed non-classification or conditional state rather than fabricate a regime.

Confidence/support is not a probability of truth unless calibrated and declared as such.


---
Copyright © 2026 Arjay Asadi. Documentation licensed under CC BY-SA 4.0 unless otherwise marked.
