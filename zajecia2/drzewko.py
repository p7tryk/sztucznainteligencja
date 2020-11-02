#!/usr/bin/env python3
""" Patryk Kaniewski
Algorytm przeszukiwania przestrzeni stanów
Wyswietlic droge:
Wyswietlic liczbe akcji
wyswietlic liczbe krokow

dla DFS dla BFS

parametryzacja (zmienna ilosc kanibali
 """

# import pdb
# pdb.set_trace()
import time

class Stan:
    def __init__(self,lk,lm,f,przodek):
        self.liczbakanibali = lk
        self.liczbamisjonarzy = lm
        self.flaga = f # f = L lodka na lewym brzegu f = P jezeli na prawym
        self.przodek = przodek
    def __str__(self):
        return str(self.liczbakanibali) + " " + str(self.liczbamisjonarzy) + " " + self.flaga

class Meta:
    def __init__(self):
        self.liczbastanow = 0
        self.dlugoschistori = 0
        self.seconds = time.time()
        self.expanded = 0
        self.compar = 0
    def __str__(self):
        return "liczba rozpatrzonych stanow " + str(self.liczbastanow) + \
            "\ndlugosc historii " + str(self.dlugoschistori) + \
            "\nwykonano w " + str((time.time() - self.seconds)) + " sekund\n" + \
            "rozszerzono do " + str(self.expanded) + " stanow\n" + \
            "porownano " + str(self.compar) + " razy"





def znajdzRozwiazanie(currentState,MAXLODKA, mode):
    """ przyjmuje stan poczatkowy i zwraca stan koncwy lub None jezeli nie mozliwy """
    MAXKANIBALI=currentState.liczbakanibali
    MAXMISJONARZY=currentState.liczbamisjonarzy
    historia = []
    lista = []
    historia.append(currentState)
    rozpatrzonych_stanow = 0

    def czyRozwiazanie(stan):
        return stan.liczbakanibali == 0 and stan.liczbamisjonarzy == 0 and stan.flaga=='P'
    
    def ekspansja(stan):
        # dostepne akcje:
        # liczbamisjonarzy+liczba.kanibali<rozmiar
        templist = []

        if stan.flaga == 'L':
            for i in range(0,MAXKANIBALI):
                for n in range(0,MAXMISJONARZY):
                    if i+n<=MAXLODKA and i+n > 0:
                        s1=Stan(stan.liczbakanibali-i,stan.liczbamisjonarzy-n,'P',stan)
                        templist.append(s1)
        else:
            for i in (0,MAXKANIBALI):
                for n in range(0,MAXMISJONARZY):
                    if i+n<=MAXLODKA and i+n > 0:
                        s1=Stan(stan.liczbakanibali-i,stan.liczbamisjonarzy-n,'L',stan)
                        templist.append(s1)
        metastats.expanded+=len(templist)
        return templist

    def filtracja(inputlist,historia):
        templist = []
        for stan in inputlist:
            if(checkHistoria(stan, historia)):
                if(stan.liczbakanibali>=0 and MAXKANIBALI-stan.liczbakanibali >=0 and stan.liczbamisjonarzy >=0 and MAXMISJONARZY -stan.liczbamisjonarzy>=0):
                    if (stan.liczbamisjonarzy<= MAXMISJONARZY and MAXMISJONARZY-stan.liczbamisjonarzy<= MAXMISJONARZY and stan.liczbakanibali<=MAXKANIBALI and MAXKANIBALI-stan.liczbakanibali<=MAXKANIBALI ):
                        if ((stan.liczbamisjonarzy==0 or stan.liczbamisjonarzy>=stan.liczbakanibali) and (stan.liczbamisjonarzy==MAXMISJONARZY or MAXMISJONARZY-stan.liczbamisjonarzy >= MAXKANIBALI-stan.liczbakanibali)):
                            templist.append(stan)
        return templist

    def checkHistoria(currentState,historia):
        for stan in historia:
            if currentState.liczbakanibali == stan.liczbakanibali \
               and currentState.liczbakanibali == stan.liczbakanibali \
               and currentState.flaga == stan.flaga:
                return False
        return True

    def wybierzWezelBFS():
        return lista.pop(0)

    def wybierzWezelDFS():
        return lista.pop(-1)

    while True:
        if debug:
            print (currentState)
        if czyRozwiazanie(currentState):
            print("sucess")
            return currentState
        metastats.liczbastanow+=1
        tmp = ekspansja(currentState)
        if debug:
            print("rozszerzono stan " + str(currentState) + " o " + str(len(tmp)) + " elementow")
        tmp = filtracja(tmp,historia)
        if debug:
            print("po filtracji dodano "+ str(len(tmp)) + " elementow")
        historia.extend(tmp)
        lista.extend(tmp)
        if not lista:
            print("nie ma rozwiazania")
            return None
        else:
            if mode == "dfs":
                currentState = wybierzWezelDFS()
            else:
                if debug:
                    print("debug " + str(lista[-1]))
                #print(len(lista))
                currentState = wybierzWezelBFS()
                #print(len(lista))
        metastats.dlugoschistori = len(historia)


def wypiszRozwiazanie(currentState):
    """Wypisuje ciag rozwiazania albo informacje ze nie ma"""

    liczba = 0

    print("Rozwiazanie:")
    if currentState is not None:
        while currentState is not None:
            liczba+=1
            print(currentState)
            currentState = currentState.przodek
    else:
        print("Nie ma rozwiazania")

    print("liczba krokow do rozwiazania " + str(liczba))
    return liczba



#BEGIN
print("Hello World!")

debug = True

state = Stan(3,3,'L', None)
metastats = Meta()

wypiszRozwiazanie(znajdzRozwiazanie(state,2,"bfs"))
print(metastats)
