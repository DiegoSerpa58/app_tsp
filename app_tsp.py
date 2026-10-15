import streamlit as st
import math
import itertools
import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Simulador TSP: O(n!) vs O(n²)", layout="wide")

st.title(" Simulador del Problema del Viajante (TSP)")
st.markdown("""
Esta aplicación interactiva te permite visualizar el crecimiento factorial **$O(n!)$** del Problema del Viajante. 
Compara el algoritmo de **Fuerza Bruta** (ruta óptima garantizada) contra la heurística del **Vecino Más Cercano** (ruta aproximada muy rápida).
""")

# --- FUNCIONES BASE ---
def calcular_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calcular_costo_ruta(ruta, ciudades):
    costo = 0
    for i in range(len(ruta)):
        costo += calcular_distancia(ciudades[ruta[i-1]], ciudades[ruta[i]])
    return costo

# --- ALGORITMOS ---
def tsp_fuerza_bruta(ciudades):
    n = len(ciudades)
    nodos = list(range(n))
    mejor_ruta = None
    menor_costo = float('inf')
    
    # Fijamos el nodo 0 como inicio para reducir simetrías, evaluamos (n-1)! permutaciones
    for perm in itertools.permutations(nodos[1:]):
        ruta_actual = [0] + list(perm)
        costo_actual = calcular_costo_ruta(ruta_actual, ciudades)
        
        if costo_actual < menor_costo:
            menor_costo = costo_actual
            mejor_ruta = ruta_actual
            
    return mejor_ruta, menor_costo

def tsp_vecino_mas_cercano(ciudades):
    n = len(ciudades)
    no_visitados = set(range(1, n))
    ruta = [0]
    nodo_actual = 0
    costo_total = 0
    
    while no_visitados:
        siguiente_nodo = min(no_visitados, key=lambda x: calcular_distancia(ciudades[nodo_actual], ciudades[x]))
        costo_total += calcular_distancia(ciudades[nodo_actual], ciudades[siguiente_nodo])
        ruta.append(siguiente_nodo)
        no_visitados.remove(siguiente_nodo)
        nodo_actual = siguiente_nodo
        
    # Volver al inicio
    costo_total += calcular_distancia(ciudades[nodo_actual], ciudades[0])
    return ruta, costo_total

# --- UI DE LA APLICACIÓN ---
st.sidebar.header("Parámetros del Simulador")
n_ciudades = st.sidebar.slider("Número de Ciudades (n)", min_value=3, max_value=12, value=6)

st.sidebar.warning("⚠️ Nota: Con n > 9, la Fuerza Bruta puede tardar varios segundos debido a que el espacio de búsqueda crece factorialmente.")

# Generar coordenadas aleatorias
if 'n_ciudades_previo' not in st.session_state or st.session_state.n_ciudades_previo != n_ciudades or st.sidebar.button("Generar Nuevo Mapa"):
    st.session_state.ciudades = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n_ciudades)]
    st.session_state.n_ciudades_previo = n_ciudades

ciudades = st.session_state.ciudades

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Evaluación: Fuerza Bruta $O(n!)$")
    st.markdown(f"Evaluando **{math.factorial(n_ciudades-1):,}** rutas posibles (fijando el nodo de inicio).")
    
    inicio_tiempo = time.time()
    ruta_optima, costo_optimo = tsp_fuerza_bruta(ciudades)
    fin_tiempo = time.time()
    tiempo_fb = fin_tiempo - inicio_tiempo
    
    st.success(f"**Costo Óptimo:** {costo_optimo:.2f}")
    st.info(f"**Tiempo de ejecución:** {tiempo_fb:.5f} segundos")
    
    # Gráfica Fuerza Bruta
    fig_fb, ax_fb = plt.subplots()
    x = [ciudades[i][0] for i in ruta_optima] + [ciudades[ruta_optima[0]][0]]
    y = [ciudades[i][1] for i in ruta_optima] + [ciudades[ruta_optima[0]][1]]
    ax_fb.plot(x, y, marker='o', color='blue', linestyle='-')
    ax_fb.plot(ciudades[0][0], ciudades[0][1], marker='s', color='red', markersize=10, label="Inicio")
    for i, txt in enumerate(ruta_optima):
        ax_fb.annotate(f"C{txt}", (ciudades[txt][0]+2, ciudades[txt][1]+2))
    ax_fb.set_title("Ruta Óptima (Garantizada)")
    st.pyplot(fig_fb)

with col2:
    st.subheader("2. Evaluación: Vecino Más Cercano $O(n^2)$")
    st.markdown(f"Evaluando decisiones locales rápidamente (aprox. **{n_ciudades**2}** iteraciones).")
    
    inicio_tiempo = time.time()
    ruta_aprox, costo_aprox = tsp_vecino_mas_cercano(ciudades)
    fin_tiempo = time.time()
    tiempo_vmc = fin_tiempo - inicio_tiempo
    
    # Calcular diferencia porcentual con la óptima
    diferencia = ((costo_aprox - costo_optimo) / costo_optimo) * 100
    
    st.warning(f"**Costo Aproximado:** {costo_aprox:.2f} (+{diferencia:.1f}% vs Óptimo)")
    st.info(f"**Tiempo de ejecución:** {tiempo_vmc:.5f} segundos")
    
    # Gráfica Vecino Más Cercano
    fig_vmc, ax_vmc = plt.subplots()
    x = [ciudades[i][0] for i in ruta_aprox] + [ciudades[ruta_aprox[0]][0]]
    y = [ciudades[i][1] for i in ruta_aprox] + [ciudades[ruta_aprox[0]][1]]
    ax_vmc.plot(x, y, marker='o', color='orange', linestyle='--')
    ax_vmc.plot(ciudades[0][0], ciudades[0][1], marker='s', color='red', markersize=10, label="Inicio")
    for i, txt in enumerate(ruta_aprox):
        ax_vmc.annotate(f"C{txt}", (ciudades[txt][0]+2, ciudades[txt][1]+2))
    ax_vmc.set_title("Ruta Heurística (Suficientemente Buena)")
    st.pyplot(fig_vmc)

# --- GRÁFICA DE COMPLEJIDAD ---
st.divider()
st.subheader("s Comparación de Complejidad: ¿Por qué la Fuerza Bruta colapsa?")

x_n = np.arange(1, 13)
y_fact = [math.factorial(i) for i in x_n]
y_quad = [i**2 for i in x_n]

fig_comp, ax_comp = plt.subplots(figsize=(10, 4))
ax_comp.plot(x_n, y_fact, label="Fuerza Bruta O(n!)", color='red', marker='x')
ax_comp.plot(x_n, y_quad, label="Vecino Más Cercano O(n²)", color='green', marker='o')
ax_comp.set_yscale('log') # Usamos escala logarítmica porque el factorial crece demasiado rápido
ax_comp.set_xlabel("Número de Ciudades (n)")
ax_comp.set_ylabel("Operaciones (Escala Logarítmica)")
ax_comp.set_title("Crecimiento de Operaciones Computacionales")
ax_comp.grid(True, which="both", ls="--", alpha=0.5)
ax_comp.legend()

st.pyplot(fig_comp)

st.markdown("""
### Conclusiones Interactivas:
* **Escalabilidad:** Modifica el control deslizante a la izquierda. Observa que para `n=5` o `n=6`, la Fuerza Bruta es instantánea. Pero al llegar a `n=10`, el tiempo de procesamiento se hace evidente para la computadora.
* **Calidad vs. Tiempo:** La heurística del Vecino Más Cercano rara vez dibuja el mapa perfecto (como se ve en la diferencia de costo), pero su tiempo de ejecución se mantiene cercano a los $0.000$ segundos sin importar si aumentas las ciudades, haciéndola vital para sistemas en tiempo real (logística, GPS).
""")