class Articulo:
    def __init__(self, valor, peso):
        if valor < 0:
            raise ValueError("El valor debe ser mayor o igual a cero")
        if peso <= 0:
            raise ValueError("El peso debe ser mayor que cero")
        self.valor = valor
        self.peso = peso
        self.seleccionado = False

    def __str__(self):
        return f"valor = {self.valor}, " \
               f"peso = {self.peso}, " \
               f"seleccionado = {self.seleccionado}"


class Mochila:

    def __init__(self, capacidad=0):
        if capacidad < 0:
            raise ValueError("El peso maximo permitido debe ser mayor o igual a 0")
        self.articulos = []
        self.capacidad = capacidad

    def insertar_articulo(self, valor, peso):
        if valor is None or peso is None:
            raise ValueError("El artículo no puede ser None")
        if self.capacidad == 0 and peso > 0:
            raise ValueError("No se pueden agregar artículos con peso positivo si la capacidad es cero")
        if valor < 0:
            raise ValueError("El valor debe ser mayor o igual a 0")
        if peso <= 0:
            raise ValueError("El peso debe ser mayor que 0")
        art = Articulo(valor, peso)
        self.articulos.append(art)

    def suma_valores(self, sumar_todos=False):
        suma = 0
        for art in self.articulos:
            if art.seleccionado or sumar_todos:
                suma += art.valor
        return suma

    def suma_pesos(self, sumar_todos=False):
        suma = 0
        for art in self.articulos:
            if art.seleccionado or sumar_todos:
                suma += art.peso
        return suma

    def valor(self):
        if self.suma_pesos() > self.capacidad:
            return -1
        else:
            return self.suma_valores()

    def articulo_de_max_valor(self, peso_disponible):
        max_valor = 0
        i = -1
        for j in range(len(self.articulos)):
            if (not self.articulos[j].seleccionado and
                    self.articulos[j].valor > max_valor and
                    self.articulos[j].peso <= peso_disponible):
                max_valor = self.articulos[j].valor
                i = j
        return i

    def imprimir(self, imprimir_todos=True):
        for i, art in enumerate(self.articulos):
            if art.seleccionado or imprimir_todos:
                print(f"articulo {i}: {art}")
        print(f"Máximo peso permitido: {self.capacidad}\n")