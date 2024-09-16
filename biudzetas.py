import pickle
from models.pajamu_irasas import PajamuIrasas
from models.islaidu_irasas import IslaiduIrasas

class Biudzetas:
    def __init__(self):
        self.zurnalas = self.gauti_is_failo()

    def irasyti_faila(self):
        with open("biudzetas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def gauti_is_failo(self):
        try:
            with open("biudzetas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except FileNotFoundError:
            zurnalas = []
        return zurnalas

    def prideti_pajamu(self):
        suma = abs(float(input("Suma: ")))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_faila()

    def prideti_islaidu(self):
        suma = abs(float(input("Suma: ")))
        budas = input("Mokėjimo būdas: ")
        isigyta = input("Įsigyta prekė/paslauga: ")
        irasas = IslaiduIrasas(suma, budas, isigyta)
        self.zurnalas.append(irasas)
        self.irasyti_faila()

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                suma -= irasas.suma
        print("Balansas:", suma)

    def atspausdinti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)