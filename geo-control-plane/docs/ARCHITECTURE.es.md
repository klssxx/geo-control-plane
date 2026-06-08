🌐 **Language:** [English](ARCHITECTURE.md) · [Español](ARCHITECTURE.es.md)

# ARQUITECTURA

GEO Control Plane es un modelo de frontera para agentes de codificación de IA.

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

## Capas

| capa | función |
| --- | --- |
| Control Plane | clasificar intención, riesgo, alcance y puertas |
| Compresión semántica | preservar restricciones al comprimir prompts |
| Política de divergencia | mantener ideas creativas separadas de la ejecución |
| Capa de enrutamiento | elegir `AUDIT`, `PLAN`, `DOCS`, `CODE`, `VALIDATE`, `DIVERGE` o `RED_REVIEW` |
| Contrato de salida | separar hechos, inferencias, incertidumbres y recomendaciones |
| Verificación en ejecución | confirmar soporte antes de actuar |
| Reversión y recuperación | requerir ruta de restauración antes de cambios materiales |
| Control de expansión | requerir evidencia, validación, respaldo y aprobación humana |

## Principio de diseño

Una ruta por operación. Una puerta por acción riesgosa. Una ruta de reversión por cambio material.
