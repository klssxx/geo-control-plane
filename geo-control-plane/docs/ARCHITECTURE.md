# ARCHITECTURE

GEO Control Plane is a boundary model for AI coding agents.

```text
HUMAN OWNER
└── GEO CONTROL PLANE
    ├── intent intake
    ├── constraint intake
    ├── risk intake
    ├── scope intake
    ├── route selection
    ├── gate enforcement
    ├── validation
    └── rollback
```

## Layers

| layer | job |
| --- | --- |
| Control Plane | classify intent, risk, scope, and gates |
| Semantic Compression | preserve constraints when compressing prompts |
| Divergence Policy | keep creative ideas separate from execution |
| Routing Layer | choose `AUDIT`, `PLAN`, `DOCS`, `CODE`, `VALIDATE`, `DIVERGE`, or `RED_REVIEW` |
| Output Contract | separate facts, inferences, uncertainties, and recommendations |
| Runtime Verification | confirm support before action |
| Rollback and Recovery | require restoration path before material changes |
| Expansion Control | require evidence, validation, backup, and human approval |

## Design Principle

One route per operation. One gate per risky action. One rollback path per material change.

