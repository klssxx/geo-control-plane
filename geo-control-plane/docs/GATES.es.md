🌐 **Language:** [English](GATES.md) · [Español](GATES.es.md)

# PUERTAS (GATES)

Las puertas son cadenas literales de autorización. Una paráfrasis no basta.

| puerta | permite |
| --- | --- |
| `AUTHORIZE_GEO_WORKSPACE_DOC_WRITE` | escritura de documentación y políticas dentro del alcance aprobado |
| `AUTHORIZE_GEO_VALIDATION_EXECUTION` | comandos de validación no destructivos |
| `AUTHORIZE_GEO_CODE_WORKTREE_PHASE` | cambios de código limitados en un worktree explícito |
| `AUTHORIZE_GEO_PACKAGE_CHANGE_PHASE` | instalación, eliminación o actualización de paquetes |
| `AUTHORIZE_GEO_GRAPHICS_STACK_PHASE` | cambios de gráficos, controladores, pantalla o arranque |

## Reglas de las puertas

- Las puertas aplican solo a su alcance nombrado.
- Las puertas no eliminan la necesidad de respaldo y reversión.
- El trabajo de alto riesgo debe comenzar como `RED_REVIEW`.
- Las acciones no soportadas deben marcarse como no soportadas, no estimarse.
