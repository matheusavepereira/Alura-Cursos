class Veiculo:
    def __init__(self,marca,modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    @property
    def ligado(self):
        return "Ligado" if self._ligado else "Desligado"

    def __str__(self):
        return f"Marca : {self._marca} | Modelo: {self._modelo} | Estado: {self.ligado}"

    