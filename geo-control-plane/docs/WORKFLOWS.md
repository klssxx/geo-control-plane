🌐 **Language:** [English](WORKFLOWS.md) · [Español](WORKFLOWS.es.md)

# WORKFLOWS

## AUDIT

Use `AUDIT` to inspect state without writing.

```text
Audit this repository for duplicated safety rules.
```

Output should list facts, inferences, uncertainties, and recommendations.

## PLAN

Use `PLAN` to design a change without executing it.

```text
Plan a safe documentation cleanup with backup and rollback.
```

## CODE

Use `CODE` only after authorization.

```text
AUTHORIZE_GEO_CODE_WORKTREE_PHASE
```

CODE must stay inside the explicit worktree.

## VALIDATE

Use `VALIDATE` to verify real results.

```bash
python scripts/validate_yaml.py
```

## DIVERGE

Use `DIVERGE` for rare, useful alternatives. Do not accept them until critique and validation.

## RED_REVIEW

Use `RED_REVIEW` for high-risk requests, incomplete rollback, unsafe permissions, or system-level changes.

