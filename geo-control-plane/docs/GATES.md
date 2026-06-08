# GATES

Gates are literal authorization strings. A paraphrase is not enough.

| gate | permits |
| --- | --- |
| `AUTHORIZE_GEO_WORKSPACE_DOC_WRITE` | documentation and policy writes inside approved scope |
| `AUTHORIZE_GEO_VALIDATION_EXECUTION` | non-destructive validation commands |
| `AUTHORIZE_GEO_CODE_WORKTREE_PHASE` | bounded code changes in an explicit worktree |
| `AUTHORIZE_GEO_PACKAGE_CHANGE_PHASE` | package install, remove, or upgrade |
| `AUTHORIZE_GEO_GRAPHICS_STACK_PHASE` | graphics, driver, display, or boot-related changes |

## Gate Rules

- Gates apply only to their named scope.
- Gates do not remove the need for backup and rollback.
- High-risk work should start as `RED_REVIEW`.
- Unsupported actions must be marked unsupported, not guessed.

