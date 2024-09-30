import pytest
import csv
import time
from random import randint
from mochila.mochila import Mochila
from mochila.busqueda_con_poda import busqueda_con_poda
from mochila.busqueda_exhaustiva import busqueda_exhaustiva
from mochila.algoritmo_voraz import algoritmo_voraz

def genera_aleatorio(num_articulos, valor_min=1, valor_max=100, peso_min=1, peso_max=100):
    if num_articulos <= 0:
        raise ValueError("El número de artículos debe ser mayor que cero")

    # Generar los artículos aleatorios
    articulos = []
    for _ in range(num_articulos):
        valor = randint(valor_min, valor_max)
        peso = randint(peso_min, peso_max)
        articulos.append((valor, peso))

    # Capacidad de la mochila
    suma_pesos = sum(peso for _, peso in articulos)
    capacidad_mochila = suma_pesos // 2

    # Creamos una instancia Mochila
    mochila = Mochila(capacidad=capacidad_mochila)

    # Agregamos los artículos a la mochila
    for valor, peso in articulos:
        mochila.insertar_articulo(valor, peso)

    return mochila

def test_busqueda_con_poda():
    for _ in range(100):
        num_articulos = randint(5, 10)
        mochila = genera_aleatorio(num_articulos)

        # Solución con búsqueda con poda
        solucion_poda, valor_poda = busqueda_con_poda(mochila)

        # Solución con búsqueda exhaustiva
        solucion_exhaustiva, valor_exhaustiva = busqueda_exhaustiva(mochila)

        # Comparación
        assert valor_poda == valor_exhaustiva, f"Fallo en búsqueda con poda: {valor_poda} != {valor_exhaustiva}"

    print("test_busqueda_con_poda pasó con éxito")

def test_algoritmo_voraz():
    for _ in range(100):
        num_articulos = randint(5, 10)
        mochila = genera_aleatorio(num_articulos)

        # Solución con algoritmo voraz
        solucion_voraz, valor_voraz = algoritmo_voraz(mochila)

        # Solución con búsqueda exhaustiva
        solucion_exhaustiva, valor_exhaustiva = busqueda_exhaustiva(mochila)

        # Comparación
        assert valor_voraz == valor_exhaustiva, f"Fallo en algoritmo voraz: {valor_voraz} != {valor_exhaustiva}"

    print("test_algoritmo_voraz pasó con éxito")

def test_escalabilidad_exhaustiva_vs_poda():
    resultados_exhaustiva = []
    resultados_poda = []

    for num_articulos in range(5, 18):
        mochila = genera_aleatorio(num_articulos)

        # Tiempo busqueda_exhaustiva
        start_time = time.time()
        solucion_exhaustiva, valor_exhaustiva = busqueda_exhaustiva(mochila)
        tiempo_exhaustiva = time.time() - start_time
        resultados_exhaustiva.append(["busqueda_exhaustiva", num_articulos, valor_exhaustiva, tiempo_exhaustiva])

        # Tiempo busqueda_con_poda
        start_time = time.time()
        solucion_poda, valor_poda = busqueda_con_poda(mochila)
        tiempo_poda = time.time() - start_time
        resultados_poda.append(["busqueda_con_poda", num_articulos, valor_poda, tiempo_poda])

    # Combinar los resultados
    resultados = resultados_exhaustiva + resultados_poda

    # Escribir los resultados en el archivo CSV
    with open('escalabilidad_exhaustiva_vs_poda.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["algoritmo", "numero_de_articulos", "valor_optimo", "segundos"])
        writer.writerows(resultados)

def test_escalabilidad_poda_vs_voraz():
    resultados_poda = []
    resultados_voraz = []

    for num_articulos in range(5, 35):
        mochila = genera_aleatorio(num_articulos)

        # Tiempo busqueda_con_poda
        start_time = time.time()
        solucion_poda, valor_poda = busqueda_con_poda(mochila)
        tiempo_poda = time.time() - start_time
        resultados_poda.append(["busqueda_con_poda", num_articulos, valor_poda, tiempo_poda])

        # Tiempo algoritmo_voraz
        start_time = time.time()
        solucion_voraz, valor_voraz = algoritmo_voraz(mochila)
        tiempo_voraz = time.time() - start_time
        resultados_voraz.append(["algoritmo_voraz", num_articulos, valor_voraz, tiempo_voraz])

    # Combinar los resultados
    resultados = resultados_poda + resultados_voraz

    # Escribir los resultados en el archivo CSV
    with open('escalabilidad_poda_vs_voraz.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["algoritmo", "numero_de_articulos", "valor_optimo", "segundos"])
        writer.writerows(resultados)



# Ejecutar directamente
#if __name__ == "__main__":
#    test_escalabilidad_poda_vs_voraz()


