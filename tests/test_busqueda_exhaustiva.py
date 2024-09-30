import pytest
from mochila.mochila import Mochila, Articulo

@pytest.mark.parametrize("C, V, P, S, L", [
    ("C1", "V1", "P3", "S2", "L3"),
    ("C1", "V2", "P4", "S3", "L1"),
    ("C1", "V3", "P3", "S3", "L3"),
    ("C1", "V4", "P4", "S2", "L1"),
    ("C2", "V1", "P1", "S1", "L2"),
    ("C2", "V2", "P2", "S2", "L2"),
    ("C2", "V3", "P4", "S1", "L3"),
    ("C2", "V4", "P3", "S3", "L2"),
    ("C3", "V1", "P2", "S3", "L3"),
    ("C3", "V2", "P1", "S1", "L3"),
    ("C3", "V3", "P2", "S2", "L2"),
    ("C3", "V4", "P1", "S1", "L3"),
    ("C4", "V1", "P4", "S2", "L1"),
    ("C4", "V2", "P3", "S1", "L1"),
    ("C4", "V3", "P1", "S3", "L1"),
    ("C4", "V4", "P2", "S1", "L2"),
    ("C3", "V3", "P3", "S2", "L2"),
    ("C3", "V3", "P4", "S3", "L2"),
    ("C4", "V2", "P1", "S2", "L3"),
    ("C4", "V2", "P2", "S3", "L1")
])
def test_mochila(C, V, P, S, L):
    capacidad = {"C1": 0, "C2": 20, "C3": 1000, "C4": -1}[C]
    valor = {"V1": 0, "V2": 20, "V3": 1000, "V4": -1}[V]
    peso = {"P1": 20, "P2": 1000, "P3": 0, "P4": -1}[P]
    seleccionado = {"S1": True, "S2": False, "S3": -1}[S]
    lista = {"L1": [], "L2": [Articulo(20, 20), Articulo(30, 30)], "L3": [None]}[L]

    if capacidad < 0:
        with pytest.raises(ValueError):
            Mochila(capacidad)
        return  #Si la capacidad no es válida
    else:
        mochila = Mochila(capacidad)

    #Insertar artículos
    for art in lista:
        if art is None:
            with pytest.raises(ValueError):
                mochila.insertar_articulo(art, art)
        else:
            if capacidad == 0 and art.peso > 0:
                with pytest.raises(ValueError):
                    mochila.insertar_articulo(art.valor, art.peso)
            elif art.valor < 0 or art.peso <= 0:
                with pytest.raises(ValueError):
                    mochila.insertar_articulo(art.valor, art.peso)
            else:
                mochila.insertar_articulo(art.valor, art.peso)

    #Selección de artículos
    if capacidad == 0:
        for art in mochila.articulos:
            with pytest.raises(ValueError):
                art.seleccionado = seleccionado
    elif seleccionado != -1:
        if len(mochila.articulos) > 0:
            try:
                mochila.articulos[0].seleccionado = seleccionado
                assert mochila.articulos[0].seleccionado == seleccionado
            except ValueError:
                assert seleccionado == -1

    #Estados finales
    if capacidad == 0:
        assert mochila.capacidad == 0
        assert len(mochila.articulos) == 0
    else:
        assert mochila.capacidad >= 0
        assert len(mochila.articulos) == len([art for art in lista if art is not None])
        for art in mochila.articulos:
            assert art.valor >= 0
            assert art.peso > 0
            assert isinstance(art.seleccionado, bool)
