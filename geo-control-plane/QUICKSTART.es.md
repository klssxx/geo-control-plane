🌐 **Language:** [English](QUICKSTART.md) · [Español](QUICKSTART.es.md)

# INICIO RÁPIDO

## 1. Clona o abre el repositorio

```bash
cd geo-control-plane
```

## 2. Lee la frontera pública

Comienza con:

- `README.md`
- `docs/GATES.md`
- `docs/RUNTIME_LIMITS.md`

## 3. Ejecuta la validación

```bash
python scripts/validate_yaml.py
```

Esperado:

```text
YAML_PARSE_PASS 2
MANIFEST_INDEX_PASS
README_REGISTRATION_PASS
FILES_CHECKED 24
RESULT PASS
```

## 4. Prueba los ejemplos

- `examples/audit-only-example.md`
- `examples/safe-code-change-example.md`
- `examples/red-review-example.md`

## 5. Adapta con seguridad

Al adaptar esta plantilla:

- mantén las rutas privadas fuera de los archivos públicos
- mantén las puertas (gates) literales
- mantén la validación reproducible
- no mezcles planificación y ejecución
