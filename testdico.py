#!/usr/local/bin/python3
from Ordered_dictionnary import Ordered_Dictionnary

# def fonction1(*abc, **params):
#     print(len(params))


dico1 = {"chips" : 1, "fruit" : 3, "tareum" : "est trop bonne"}
dico2 = {"der" : 1, "frbbuit" : 3, "v" : "est tttttp bonne"}
# fonction1(a = 1, b = 2, c = 3)
toto = Ordered_Dictionnary(dico1)
titi = Ordered_Dictionnary(dico2)


toto = Ordered_Dictionnary()
print(toto)

toto["chips"] = 5
toto["tomate"] = 8

print(toto)