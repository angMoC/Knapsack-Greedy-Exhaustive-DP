def mochila_programacion_dinamica(mochila):
    n = len(mochila.articulos)
    W = mochila.capacidad
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif mochila.articulos[i-1].peso <= w:
                K[i][w] = max(mochila.articulos[i-1].valor + K[i-1][w - mochila.articulos[i-1].peso], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # Reconstruir la solución óptima
    res = K[n][W]
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i-1][w]:
            continue
        else:
            mochila.articulos[i-1].seleccionado = True
            res = res - mochila.articulos[i-1].valor
            w = w - mochila.articulos[i-1].peso

    return K[n][W]