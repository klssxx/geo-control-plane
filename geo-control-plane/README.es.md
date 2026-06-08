🌐 **Language:** [English](README.md) · [Español](README.es.md)

# GEO Control Plane

Una capa de control con prioridad de seguridad para agentes de codificación de IA.

## ¿Qué problema resuelve?

Los agentes de IA suelen mezclar la planificación, la ejecución y la validación en un solo paso. GEO Control Plane las separa en rutas explícitas y requiere puertas (gates) antes de acciones riesgosas.

## Rutas principales

| ruta | propósito |
| --- | --- |
| `AUDIT` | inspeccionar sin escribir |
| `PLAN` | proponer cambios sin ejecutarlos |
| `DOCS` | crear o limpiar documentación tras autorización |
| `CODE` | modificar archivos del espacio de trabajo tras autorización |
| `VALIDATE` | verificar resultados reales |
| `DIVERGE` | generar opciones inusuales sin aceptarlas |
| `RED_REVIEW` | desafiar propuestas inseguras o incompletas |

## Comienza aquí

1. Lee `QUICKSTART.md`.
2. Ejecuta el ejemplo de AUDIT.
3. Revisa `docs/GATES.md`.
4. Valida el manifiesto YAML:

```bash
python scripts/validate_yaml.py
```

Salida esperada:

```text
YAML_PARSE_PASS 2
MANIFEST_INDEX_PASS
README_REGISTRATION_PASS
FILES_CHECKED 24
RESULT PASS
```

## Agentes y modelos

| agente/modelo | buen uso | frontera |
| --- | --- | --- |
| `Human Owner` | aprobación final y prioridades | debe proporcionar puertas explícitas |
| `GEO Control Plane` | alcance, enrutamiento, riesgo, reversión, validación | no ejecuta por sí mismo |
| `Codex` | ediciones de código, validación de archivos, trabajo en repositorio | limitado por rutas y puertas |
| `Hermes Agent` | patrón de orquestación futuro | no habilitado en esta plantilla pública |
| LLM de alto razonamiento | revisión de arquitectura, crítica, divergencia | solo recomendaciones sin puertas |

## Qué puedes hacer con él

- Auditar un repositorio antes de permitir escrituras.
- Separar la planificación de la ejecución.
- Requerir reversión antes de cambios materiales.
- Validar archivos de control YAML.
- Documentar solicitudes de alto riesgo como `RED_REVIEW`.
- Mantener sugerencias creativas en `DIVERGE` hasta crítica y validación.

## Lo que esta plantilla NO hace

- No instala paquetes.
- No inicia servicios.
- No despacha trabajadores.
- No proporciona credenciales.
- No otorga acceso a tu sistema de archivos.

## Arquitectura

```text
HUMAN OWNER
└── GEO CONTROL PLANE
    ├── policy: GEO-MANIFEST.yaml
    ├── index: MASTER_INDEX.md
    ├── docs: docs/*.md
    ├── examples: examples/*.md
    └── validation: scripts/validate_yaml.py
```
