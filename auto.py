class Auto:
    """ Clase que implementa producto"""
    def __init__(self,placa, marca,modelo, precio) -> None:
        self.placa=placa
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
        pass
    def convertir_a_string(self):
        return "|{}|{}|{}||{}|".format(self.placa,
                                    self.marca,
                                    self.modelo,
                                    self.precio)
        