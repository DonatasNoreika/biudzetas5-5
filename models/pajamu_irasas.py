from models.irasas import Irasas

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __repr__(self):
        return f"Pajamos: {self.suma}, siuntėjas - {self.siuntejas} ({self.info})"