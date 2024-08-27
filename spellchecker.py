import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multiDic = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())

        parole = txtIn.split()

        print("---------------------------------")
        print("Using contains")
        t1 = time.time()
        prl = self._multiDic.searchWord(parole, language)

        for parola in prl:
            if parola.corretta == False:
                print(parola)

        t2 = time.time()

        print("Time elapsed " + str(t2-t1))

        print("---------------------------------")
        print("Using linear search")
        t1 = time.time()
        prl = self._multiDic.searchWordLinear(parole, language)

        for parola in prl:
            if parola.corretta == False:
                print(parola)

        t2 = time.time()

        print("Time elapsed " + str(t2-t1))

        print("---------------------------------")
        print("Using dicotomic search")

        t1 = time.time()
        prl = self._multiDic.searchWordDicotomic(parole, language)

        for parola in prl:
            if parola.corretta == False:
                print(parola)

        t2 = time.time()

        print("Time elapsed " + str(t2-t1))


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\/'*_{}[]()<>#@+-.:,;!£$%&=?^"
    for c in chars:
        text = text.replace(c, "")

    return text