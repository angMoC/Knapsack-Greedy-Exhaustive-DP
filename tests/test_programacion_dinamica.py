import pytest
import csv
import time
from random import randint
from mochila.mochila import Mochila
from mochila.busqueda_exhaustiva import busqueda_exhaustiva
from mochila.programación_dinamica import mochila_programacion_dinamica
from tests.test_algoritmos_alternativos import genera_aleatorio
from mochila.algoritmo_voraz import algoritmo_voraz

def test_programacion_dinamica():
    for _ in range(100):
        num_articulos = randint(5, 10)
        mochila = genera_aleatorio(num_articulos)

        # Solución con programación dinámica
        valor_dinamica = mochila_programacion_dinamica(mochila)

        # Solución con búsqueda exhaustiva
        _, valor_exhaustiva = busqueda_exhaustiva(mochila)

        # Comparar los valores
        assert valor_dinamica == valor_exhaustiva, f"Fallo en programación dinámica: {valor_dinamica} != {valor_exhaustiva}"

    print("test_programacion_dinamica pasó con éxito")

def test_escalabilidad_dinamica_vs_voraz():
    resultados_dinamica = []
    resultados_voraz = []

    for num_articulos in range(5, 35):
        mochila = genera_aleatorio(num_articulos)

        # Tiempo programación dinámica
        start_time = time.time()
        valor_dinamica = mochila_programacion_dinamica(mochila)
        tiempo_dinamica = time.time() - start_time
        resultados_dinamica.append(["programacion_dinamica", num_articulos, valor_dinamica, tiempo_dinamica])

        # Tiempo algoritmo voraz
        start_time = time.time()
        solucion_voraz, valor_voraz = algoritmo_voraz(mochila)
        tiempo_voraz = time.time() - start_time
        resultados_voraz.append(["algoritmo_voraz", num_articulos, valor_voraz, tiempo_voraz])

    # Combinar los resultados
    resultados = resultados_dinamica + resultados_voraz

    # Escribir los resultados en el archivo CSV
    with open('escalabilidad_dinamica_vs_voraz.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["algoritmo", "numero_de_articulos", "valor_optimo", "segundos"])
        writer.writerows(resultados)


# Ejecutar directamente
#if __name__ == "__main__":
#    test_programacion_dinamica()

#if __name__ == "__main__":
#    test_escalabilidad_dinamica_vs_voraz()