#!/usr/bin/env python3
""" Algorytm przeszukiwania przestrzeni stanów
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
    def __init__(self,ls,hist):
        self.liczbastanow = ls
        self.dlugoschistori = hist
        self.seconds = 0
    def __str__(self):
        return "liczba rozpatrzonych stanow " + str(self.liczbastanow) + "\ndlugosc historii " + str(self.dlugoschistori) + "\n"





def znajdzRozwiazanie(currentState, mode):
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
        # 2M, 2K, 1K1M, 1K, 1M
        templist = []
    
        if stan.flaga == 'L':
            if stan.liczbakanibali>1:
                s1 = Stan(stan.liczbakanibali-2,stan.liczbamisjonarzy, 'P',stan)
                templist.append(s1)
            if stan.liczbakanibali>0:
                s1 = Stan(stan.liczbakanibali-1,stan.liczbamisjonarzy, 'P',stan)
                templist.append(s1)
            if stan.liczbamisjonarzy>1:
                s1 = Stan(stan.liczbakanibali,stan.liczbamisjonarzy-2, 'P',stan)
                templist.append(s1)
            if stan.liczbamisjonarzy>0:
                s1 = Stan(stan.liczbakanibali,stan.liczbamisjonarzy-1, 'P',stan)
                templist.append(s1)
            if stan.liczbamisjonarzy>0 and stan.liczbakanibali>0:
                s1 = Stan(stan.liczbakanibali-1,stan.liczbamisjonarzy-1, 'P',stan)
                templist.append(s1)
        else:
            if MAXKANIBALI-stan.liczbakanibali>1:
                s1 = Stan(stan.liczbakanibali+2,stan.liczbamisjonarzy, 'L',stan)
                templist.append(s1)
            if MAXKANIBALI-stan.liczbakanibali>0:
                s1 = Stan(stan.liczbakanibali+1,stan.liczbamisjonarzy, 'L',stan)
                templist.append(s1)
            if MAXMISJONARZY-stan.liczbamisjonarzy>1:
                s1 = Stan(stan.liczbakanibali,stan.liczbamisjonarzy+2, 'L',stan)
                templist.append(s1)
            if MAXMISJONARZY-stan.liczbamisjonarzy>0:
                s1 = Stan(stan.liczbakanibali,stan.liczbamisjonarzy+1, 'L',stan)
                templist.append(s1)
            if MAXMISJONARZY-stan.liczbamisjonarzy>0 and MAXKANIBALI-stan.liczbakanibali>0:
                s1 = Stan(stan.liczbakanibali+1,stan.liczbamisjonarzy+1, 'L',stan)
                templist.append(s1)
        return templist

    def filtracja(inputlist):
        templist = []
        for stan in inputlist:
            if ((stan.liczbamisjonarzy==0 or stan.liczbamisjonarzy>=stan.liczbakanibali)and (stan.liczbamisjonarzy==MAXMISJONARZY or MAXMISJONARZY-stan.liczbamisjonarzy >= MAXKANIBALI-stan.liczbakanibali)and stan not in lista):
                templist.append(stan)
        return templist

    def wybierzWezelDFS():
        return lista.pop(0)

    def wybierzWezelBFS():
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
        tmp = filtracja(tmp)
        if debug:
            print("po filtracji dodano "+ str(len(tmp)) + " elementow")
        historia.extend(tmp)
        lista.extend(tmp)
        if not lista:
            print("nie ma rozwiazania")
            return None
        else:
            if mode == "dfs" or len(lista) < 10:
                currentState = wybierzWezelDFS()
            else:
                if debug:
                    print("debug " + str(lista[-1]))
                currentState = wybierzWezelBFS()
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

debug = False
state = Stan(4,4,'L', None)
metastats = Meta(0,0)
wypiszRozwiazanie(znajdzRozwiazanie(state,"dfs"))
print(metastats)
