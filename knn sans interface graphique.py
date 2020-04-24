""" Presentation Du Projet : Simulation de réfrigérateur a l'aide d'un algorithme style 'k plus proches voisins'//
Cette algo a pour but de comparer les réfrigérateurs d'une population par rapport a la votre, votre frigo etant la liste nommé: témoin[]// Pour afficher les réfrigérateurs qui sont comparés au votre pressez f5 puis appelez la liste prsn[], ces réfrigérateurs seront numérotés selon le nombre de 'gens' que vous avez choisi a la ligne 88 dans la fonction gens(x)et en deuxieme arguments de la ligne 258 le nombre de k voisins voulu
"""
import random
from tkinter import *

ingredient=['sauces','yaourts','fruits','legumes','viandes','eau','soda','glace','fromage','lait']

temoin=['sauces','yaourts','fruits']

prsn=[]

def gens(num):
    var = 1
    secu=[]
    prsn.clear()
    for i in range(num):
        a = random.randint(0,len(ingredient)-1)
        while a == 0:
            a = random.randint(0,len(ingredient)-1)
        b=frigo(a)
        if b in secu:
            b=frigo(a)
        b.append(var)
        var = var +1
        prsn.append(b)
        secu.append(b)


def frigo(num):
    L=[]
    cuse=[]
    for i in range (num):
        a=random.randint(0,len(ingredient)-1)
        b=ingredient[a]
        if b in L:
            a=random.randint(0,len(ingredient)-1)
            b=ingredient[a]
        else:
            L.append(b)
    return L


def knn(temoin):
    vide=[]
    for elt in temoin:
        for i in range (len(prsn) - 1):
            a = prsn[i]
            for elts in a:
                if  elt == elts:
                    if a not in vide:
                        vide.append(a)
    c=len(vide)
    dede=''
    for i in range(c):
        d=vide[i]
        x=d[-1]
        dede=dede+str(x)+","
    if len(dede) == 2:
        print("le frigo similaire au votre est le numero: "+dede)
    if len(dede) > 2:
        print('les frigos similaires au votre ont le numero:'+dede)
    if vide==[]:
        print('aucun frigo similaire au votre')
    return vide


def autre(prsn,vide):
    zzz= []
    for item in prsn:
        if item not in vide:
            zzz.append(item)
    return zzz


def voisin(vide,K):
    if K > len(vide):
        print("vous avez dépassé le nombre d'element de la liste")
    else:
        T=vide[:K]
    beto=''
    for elt in T:
        q = elt[-1]
        beto = beto + str(q) + ','
    print("les "+ " " + str(K)+" "+" plus proches voisins sont les numeros " + beto)

""" changez la valeur de l'argument de la fonction gens() pour avoir le nombre de frigo que l'on allons comparer aux votres et le deuxieme argument de voisin() pour avoir les k plus proches voisins voulu"""
gens(85)
vide = knn(temoin)
voisin(vide,3)
sss = autre(prsn,vide)
vide.extend(sss)