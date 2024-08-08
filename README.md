# Analizador de Logs

Este proyecto es un script en Python que lee archivos de log en una carpeta específica, identifica los logs que contienen el mensaje "Iniciem el Servei de connexió TCP" en `<CAMPO9>`, y muestra la fecha en la que se inició el servicio.

## Cómo usar

1. Coloca tus archivos de log en la carpeta `logs/`. Los archivos de log deben tener una extensión numérica (por ejemplo, `BBDDVirtual.1`, `BBDDVirtual.2`).
2. Ejecuta el script `log_analyzer.py`.
3. El script imprimirá en la terminal la fecha y hora en que se inició el servicio, ordenadas de la más reciente a la más antigua.

## Requisitos

- Python 3.x

## Ejecución

```bash
python log_analyzer.py
```

