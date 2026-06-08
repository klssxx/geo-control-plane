🌐 **Language:** [English](WORKFLOWS.md) · [Español](WORKFLOWS.es.md)

# FLUJOS DE TRABAJO

## AUDIT

Usa `AUDIT` para inspeccionar el estado sin escribir.

```text
Audit this repository for duplicated safety rules.
```

La salida debe listar hechos, inferencias, incertidumbres y recomendaciones.

## PLAN

Usa `PLAN` para diseñar un cambio sin ejecutarlo.

```text
Plan a safe documentation cleanup with backup and rollback.
```

## CODE

Usa `CODE` solo tras autorización.

```text
AUTHORIZE_GEO_CODE_WORKTREE_PHASE
```

CODE debe permanecer dentro del worktree explícito.

## VALIDATE

Usa `VALIDATE` para verificar resultados reales.

```bash
python scripts/validate_yaml.py
```

## DIVERGE

Usa `DIVERGE` para alternativas raras y útiles. No las aceptes hasta crítica y validación.

## RED_REVIEW

Usa `RED_REVIEW` para solicitudes de alto riesgo, reversión incompleta, permisos inseguros o cambios a nivel de sistema.
