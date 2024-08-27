import dictionary as d
import richWord as rw




class MultiDictionary:

    def __init__(self):
        self._inglese = d.Dictionary([], "english")
        self._italiano = d.Dictionary([], "italian")
        self._spagnolo = d.Dictionary([], "spanish")

        self._inglese.loadDictionary("resources/English.txt")
        self._italiano.loadDictionary("resources/Italian.txt")
        self._spagnolo.loadDictionary("resources/Spanish.txt")


    def printDic(self, language):
        if language=="english":
            self._inglese.printAll()
        elif language=="italian":
            self._italiano.printAll()
        elif language=="spanish":
            self._spagnolo.printAll()
        else:
            print("Lingua non supportata")

    def searchWord(self, words, language):

       parole = []

       for parola in words:
           parola = parola.lower()
           found = False
           rich_word = rw.RichWord(parola)

           if language == "english":
               if self._inglese.dict.__contains__(parola):
                   found = True
           elif language == "italian":
               if self._italiano.dict.__contains__(parola):
                   found = True
           elif language == "spanish":
               if self._spagnolo.dict.__contains__(parola):
                   found = True

           if found:
               rich_word.corretta = True

           parole.append(rich_word)

       return parole

    def searchWordLinear(self, words, language):

        parole = []

        for parola in words:
            parola = parola.lower()
            found = False
            rich_word = rw.RichWord(parola)

            if language == "english":
                for word in self._inglese.dict:
                    if word==parola:
                        found = True
            elif language == "italian":
                for word in self._italiano.dict:
                    if word == parola:
                        found = True
            elif language == "spanish":
                for word in self._spagnolo.dict:
                    if word == parola:
                        found = True

            if found:
                rich_word.corretta = True

            parole.append(rich_word)

        return parole

    def searchWordDicotomic(self, words, language):

        parole = []

        for parola in words:
            parola = parola.lower()
            found = False
            rich_word = rw.RichWord(parola)

            if language == "english":
                diz = self._inglese.dict
                found = self.ricerca_dicotomica(parola, diz)
            elif language == "italian":
                diz = self._italiano.dict
                found = self.ricerca_dicotomica(parola, diz)
            elif language == "spanish":
                diz = self._spagnolo.dict
                found = self.ricerca_dicotomica(parola, diz)

            if found:
                rich_word.corretta = True

            parole.append(rich_word)

        return parole

    def ricerca_dicotomica(parola, diz):
        inizio = 0
        fine = len(diz) - 1

        while inizio <= fine:
            indice_mediano = (inizio+fine)//2
            mediano = diz[indice_mediano]

            if mediano == parola:
                return True
            if mediano > parola:
                fine = indice_mediano - 1
            else:
                inizio = mediano + 1

        return False





