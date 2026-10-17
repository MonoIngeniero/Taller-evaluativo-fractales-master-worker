# Resultados monolito (A) - ejecución secuencial

## Especificaciones de la máquina

| Componente | Valor |
|---|---|
| CPU | AMD Ryzen 5 7520U with Radeon Graphics |
| Núcleos / hilos lógicos | 4 / 8 |
| RAM | 15,3 GB |
| Java | OpenJDK Temurin 21.0.12.1 (LTS) |
| ZeroC Ice | 3.7.11 |
| Ejecución | `.\gradlew.bat :monolith:runMonolith` (monohilo) |

## Configuraciones del benchmark

| # | Preset | Resolución | maxIter | Tiempo (ms) | Tiempo (min) |
|---|---|---|---|---|---|
| 1 | seahorse | 3840x2160 | 5000 | 146237 | 2,44 |
| 2 | seahorse | 3840x2160 | 10000 | 289852 | 4,83 |
| 3 | seahorse | 1920x1080 | 20000 | 145614 | 2,43 |
| 4 | mini | 3840x2160 | 15000 | 121020 | 2,02 |
| 5 | elephant | 3840x2160 | 10000 | 117733 | 1,96 |

## Corridas de calibración (fuera del rango de 1-10 min)

| Preset | Resolución | maxIter | Tiempo (ms) | Tiempo (min) |
|---|---|---|---|---|
| seahorse | 1280x720 | 2000 | 6900 | 0,12 |
| mini | 3840x2160 | 5000 | 39902 | 0,67 |
| elephant | 3840x2160 | 5000 | 58278 | 0,97 |

## Observaciones

- El tiempo escala de forma casi lineal con las iteraciones: seahorse 4K pasó de 146 s (5000) a 290 s (10000).
- Las corridas de mini y elephant con 5000 iteraciones quedaron por debajo de 1 min, por eso se repitieron con más iteraciones.
- Todas las ejecuciones se hicieron con el PC sin otros programas pesados abiertos.

## Evidencia

Capturas de la consola en `resultados/conexionA/`.