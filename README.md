# App TSP

Aplicación interactiva desarrollada con **Python** y **Streamlit** para estudiar y visualizar el **Problema del Viajante (TSP, por sus siglas en inglés: Travelling Salesman Problem)**.

La aplicación genera un mapa aleatorio de ciudades y compara dos estrategias para encontrar una ruta circular que visite todas las ciudades exactamente una vez y regrese al punto de inicio:

- **Fuerza bruta:** encuentra la ruta óptima, pero su costo computacional crece factorialmente.
- **Vecino más cercano:** encuentra rápidamente una ruta aproximada mediante decisiones locales.

El proyecto tiene un propósito educativo: mostrar de forma visual la diferencia entre una solución exacta y una heurística, así como el impacto práctico de las complejidades **O(n!)** y **O(n²)**.

## Características principales

- Generación de coordenadas aleatorias para las ciudades.
- Control interactivo del número de ciudades mediante un deslizador.
- Generación de nuevos mapas aleatorios.
- Resolución del TSP mediante fuerza bruta.
- Resolución aproximada mediante la heurística del vecino más cercano.
- Cálculo del costo total de cada ruta.
- Medición del tiempo de ejecución de ambos algoritmos.
- Comparación porcentual entre el resultado aproximado y el resultado óptimo.
- Visualización gráfica de las rutas encontradas.
- Gráfica comparativa del crecimiento de **O(n!)** frente a **O(n²)** usando escala logarítmica.

## Contexto del problema TSP

El Problema del Viajante consiste en encontrar la ruta de menor distancia que permita visitar un conjunto de ciudades exactamente una vez, regresar a la ciudad de origen y minimizar la distancia total recorrida.

Es un problema clásico de optimización combinatoria y pertenece a la categoría de problemas **NP-difíciles**. A medida que aumenta el número de ciudades, también aumenta rápidamente el número de rutas posibles.

En este proyecto se fija la ciudad `C0` como punto de partida. Por ello, para `n` ciudades se evalúan `(n - 1)!` permutaciones en lugar de `n!`, reduciendo las rutas equivalentes por simetría, aunque el crecimiento continúa siendo factorial.

## Algoritmos implementados

### 1. Fuerza bruta — O(n!)

La fuerza bruta genera y evalúa todas las permutaciones posibles de las ciudades, seleccionando la ruta con menor costo.

**Ventajas:**

- Garantiza encontrar la ruta óptima.
- Es sencilla de comprender y verificar.
- Resulta útil como referencia para evaluar heurísticas.

**Desventajas:**

- Su tiempo de ejecución crece factorialmente.
- Se vuelve poco práctica cuando aumenta el número de ciudades.
- En la aplicación puede tardar varios segundos para valores altos de `n`.

### 2. Vecino más cercano — O(n²)

La heurística comienza en la ciudad `C0` y, en cada paso, visita la ciudad no visitada más cercana a la posición actual. Finalmente, regresa a la ciudad de origen.

**Ventajas:**

- Es rápida y fácil de implementar.
- Tiene un costo computacional mucho menor que la fuerza bruta.
- Permite trabajar con una cantidad mayor de ciudades en menos tiempo.

**Desventajas:**

- No garantiza encontrar la ruta óptima.
- Una decisión local puede producir una ruta globalmente poco eficiente.
- La calidad de la solución depende de la distribución de las ciudades.

## Requisitos

- Python 3.9 o superior.
- `pip` para instalar las dependencias.

Dependencias utilizadas:

- [Streamlit](https://streamlit.io/): interfaz web interactiva.
- [Matplotlib](https://matplotlib.org/): generación de gráficos.
- [NumPy](https://numpy.org/): manejo de arreglos y datos numéricos.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/DiegoSerpa58/app_tsp.git
   cd app_tsp
   ```

2. Crea y activa un entorno virtual — recomendado:

   **Windows:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install streamlit matplotlib numpy
   ```

## Ejecución

Desde la carpeta raíz del proyecto, ejecuta:

```bash
streamlit run app_tsp.py
```

Streamlit abrirá la aplicación en el navegador. Si no se abre automáticamente, utiliza la dirección que muestre la terminal, normalmente:

```text
http://localhost:8501
```

## Uso de la aplicación

1. Ajusta el control **Número de Ciudades (n)** ubicado en la barra lateral.
2. Observa el mapa generado aleatoriamente.
3. Revisa la ruta óptima calculada mediante fuerza bruta.
4. Revisa la ruta aproximada calculada mediante vecino más cercano.
5. Compara el costo de ambas rutas.
6. Compara sus tiempos de ejecución.
7. Utiliza **Generar Nuevo Mapa** para crear otra distribución de ciudades.
8. Observa la gráfica de complejidad para analizar el crecimiento factorial y cuadrático.

La aplicación permite seleccionar entre **3 y 12 ciudades**. Para valores altos, la fuerza bruta puede tardar considerablemente debido al número de rutas que debe evaluar.

## Estructura del proyecto

```text
app_tsp/
├── app_tsp.py    # Aplicación Streamlit, algoritmos y visualizaciones
└── README.md     # Documentación del proyecto
```

## Funciones principales

- `calcular_distancia(p1, p2)`: calcula la distancia euclidiana entre dos ciudades.
- `calcular_costo_ruta(ruta, ciudades)`: calcula la distancia total de una ruta circular.
- `tsp_fuerza_bruta(ciudades)`: busca la ruta óptima evaluando las permutaciones posibles.
- `tsp_vecino_mas_cercano(ciudades)`: calcula una ruta aproximada usando la ciudad no visitada más cercana.

## Complejidad computacional

| Algoritmo | Complejidad aproximada | ¿Garantiza el óptimo? | Velocidad esperada |
|---|---:|---:|---:|
| Fuerza bruta | O(n!) | Sí | Baja cuando `n` crece |
| Vecino más cercano | O(n²) | No | Alta |

La aplicación utiliza una escala logarítmica en la gráfica de complejidad porque el crecimiento factorial supera rápidamente al crecimiento cuadrático.

## Limitaciones conocidas

- Las ciudades se generan de forma aleatoria dentro de un plano de coordenadas de `0` a `100`.
- La aplicación utiliza distancia euclidiana; no considera carreteras, tráfico ni restricciones geográficas reales.
- La fuerza bruta está limitada a un número reducido de ciudades por su costo computacional.
- El vecino más cercano puede producir resultados diferentes en calidad según la distribución aleatoria del mapa.
- Las dependencias todavía pueden instalarse manualmente porque el proyecto no incluye un archivo `requirements.txt`.

## Posibles mejoras

- Agregar un archivo `requirements.txt` para automatizar la instalación.
- Incorporar otras heurísticas, como 2-opt, búsqueda local o algoritmo genético.
- Permitir cargar coordenadas desde un archivo CSV.
- Añadir diferentes métricas de distancia.
- Comparar varias ejecuciones y calcular estadísticas de rendimiento.
- Implementar una matriz de distancias configurable.
- Exportar las rutas y resultados obtenidos.
- Agregar pruebas automatizadas para los algoritmos.

## Objetivo académico

Este proyecto sirve como material práctico para comprender:

- Problemas de optimización combinatoria.
- Diferencias entre algoritmos exactos y heurísticos.
- Complejidad temporal.
- Crecimiento factorial y cuadrático.
- Visualización de algoritmos.
- Relación entre calidad de una solución y tiempo de ejecución.

## Licencia

Este repositorio no declara actualmente una licencia. Si el proyecto se va a distribuir o reutilizar, se recomienda agregar una licencia explícita, por ejemplo MIT.

## Autor

Desarrollado por [DiegoSerpa58](https://github.com/DiegoSerpa58).
