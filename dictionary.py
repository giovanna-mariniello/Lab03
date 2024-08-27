class Dictionary:
    def __init__(self, dizionario=[], lingua=""):
        self._dizionario = dizionario
        self._lingua = lingua


    def loadDictionary(self, path):
        file_diz = path

        with open(file_diz, "r", encoding="utf-8") as file:
            for line in file:
                parola = line.strip()
                self._dizionario.append(parola.lower())


    def printAll(self):
        for parola in self._dizionario:
            print(f"{parola}")


    @property
    def dict(self):
        return self._dizionario