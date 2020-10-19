#!/usr/bin/env python3
""" Algorytm przeszukiwania przestrzeni stanów """

MAXKANIBALI = 3

MAXMISJONARZY = 3


class Stan:
    def __init__(self,lk,lm,f):
        self.liczbakanibali = lk
        self.liczbamisjonarzy = lm
        self.flaga = f # f = L lodka na lewym brzegu f = P jezeli na prawym
def czyRozwiazanie(stan):
    return stan.liczbakanibali == 0 and stan.liczbamisjonarzy == 0 and stan.flaga=='P'

def ekspansja(stan):
    # dostepne akcje:
    # 2M, 2K, 1K1M, 1K, 1M
    templist = []
    
    if stan.flaga == 'L':
        if stan.liczbakanibali>1:
            s1 = Stan(stan.liczbakanibali-2,stan.liczbamisjonarzy, 'P')
            templist.append(s1)
        if stan.liczbakanibali>0:
            s1 = Stan(stan.liczbakanibali-1,stan.liczbamisjonarzy, 'P')
            templist.append(s1)
        if stan.liczbamisjonarzy>1:
            s1 = Stan(stan.liczbakanibali,stan.liczbamisjonarzy-2, 'P')
            templist.append(s1)
        if stan.liczbamisjonarzy>0:
            s1 = Stan(stan.liczbakanibali,stan.liczbamisjonarzy-1, 'P')
            templist.append(s1)
        if stan.liczbamisjonarzy>0 and stan.liczbakanibali>0:
            s1 = Stan(stan.liczbakanibali-1,stan.liczbamisjonarzy-1, 'P')
            templist.append(s1)
    else:
        if MAXKANIBALI-stan.liczbakanibali>1:
            s1 = Stan(stan.liczbakanibali+2,stan.liczbamisjonarzy, 'L')
            templist.append(s1)
        if MAXKANIBALI-stan.liczbakanibali>0:
            s1 = Stan(stan.liczbakanibali+1,stan.liczbamisjonarzy, 'L')
            templist.append(s1)
        if MAXMISJONARZY-stan.liczbamisjonarzy>1:
            s1 = Stan(stan.liczbakanibali,stan.liczbamisjonarzy+2, 'L')
            templist.append(s1)
        if MAXMISJONARZY-stan.liczbamisjonarzy>0:
            s1 = Stan(stan.liczbakanibali,stan.liczbamisjonarzy+1, 'L')
            templist.append(s1)
        if MAXMISJONARZY-stan.liczbamisjonarzy>0 and MAXKANIBALI-stan.liczbakanibali>0:
            s1 = Stan(stan.liczbakanibali+1,stan.liczbamisjonarzy+1, 'L')
            templist.append(s1)
    return templist


def filtracja(inputlist):

    templist = []
    for stan in inputlist:
        if stan.liczbamisjonarzy>0:
            if stan.liczbamisjonarzy>=stan.liczbakanibali:
                templist.append(stan)
        if MAXMISJONARZY-stan.liczbamisjonarzy>0:
            if MAXMISJONARZY-stan.liczbamisjonarzy>=MAXKANIBALI-stan.liczbakanibali:
                templist.append(stan)
    return templist

def listaPusta():
    return True

def wybierzWezel():
    x=0

print("Hello World!")

currentState = Stan(3,3,'L')

historia = []

lista = []

while True:
    if czyRozwiazanie(currentState):
        break
    tmp = ekspansja(currentState)
    tmp = filtracja(tmp)
    if listaPusta():
        break
    wybierzWezel()
