from models.irasas import Irasas

class IslaiduIrasas(Irasas):
    def __init__(self, suma, budas, isigyta):
        super().__init__(suma)
        self.budas = budas
        self.isigyta = isigyta

    def __repr__(self):
        return f"Išlaidos: {self.suma}, mokėjimo būdas - {self.budas}, įsigyta - {self.isigyta}"