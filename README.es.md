🌐 **Language:** [English](README.md) · [Español](README.es.md)

# GEO Control Plane — Edición Pública

Una plantilla de orquestación con prioridad de seguridad para agentes de codificación de IA.

## ¿Qué problema resuelve?

Los agentes de IA suelen mezclar la planificación, la ejecución y la validación en un solo paso. GEO Control Plane las separa en rutas explícitas y requiere puertas (gates) antes de realizar acciones riesgosas.

## Rutas principales

- `AUDIT` - inspeccionar sin escribir
- `PLAN` - proponer cambios sin ejecutarlos
- `CODE` - modificar archivos del espacio de trabajo tras autorización
- `VALIDATE` - verificar resultados reales
- `DIVERGE` - generar opciones inusuales sin aceptarlas
- `RED_REVIEW` - desafiar propuestas inseguras o incompletas

## Comienza aquí

1. Lee [QUICKSTART.md](geo-control-plane/QUICKSTART.md).
2. Ejecuta el [ejemplo de AUDIT](geo-control-plane/examples/audit-only-example.md).
3. Revisa el [modelo de puertas](geo-control-plane/docs/GATES.md).
4. Valida el manifiesto YAML:

```bash
cd geo-control-plane
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

## Posición de seguridad pública

Esta edición pública es solo documentación y validación. No incluye volcados de ejecución, credenciales, respaldos, prompts privados, registros de paquetes, claves de API ni configuración específica de máquina.

## Estructura del repositorio

```text
geo-control-plane/
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── GEO-MANIFEST.yaml
├── MASTER_INDEX.md
├── QUICKSTART.md
├── docs/
├── examples/
└── scripts/
```

También se incluyen archivos a nivel de repositorio: `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.gitignore` y `.github/workflows/validate.yml`.
