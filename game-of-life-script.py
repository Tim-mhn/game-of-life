import tkinter 
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from math import *
import time


#on code le jeu de la vie avec une matrice qui servira de répresentation mathématique du quadrillage
#une case coloriée correspond à un 1 dans la matrice

Cote = 400
Nb = 3
pas = Cote/Nb

def nb_voisin(M,i,j):
    if i==0:
        if j==0:
            return(M[1][0]+M[1][1]+M[0][1])
        if j==Nb-1:
            return(M[0][Nb-2]+M[1][Nb-2]+M[1][Nb-1])
        else:
            return(M[0][j-1]+M[1][j-1]+M[1][j]+M[1][j+1]+M[0][j+1])
    
    if i==Nb-1:
        if j==0:
            return(M[Nb-2][0]+M[Nb-2][1]+M[Nb-1][1])
        if j==Nb-1:
            return(M[Nb-1][Nb-2]+M[Nb-2][Nb-2]+M[Nb-2][Nb-1])
        else:
            return(M[i][j-1]+M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j+1])
            
    if j==0:
        return(M[i-1][j]+M[i-1][j+1]+M[i][j+1]+M[i+1][j+1]+M[i+1][j])
    
    if j==Nb-1:
        return(M[i-1][j]+M[i-1][j-1]+M[i][j-1]+M[i+1][j-1]+M[i+1][j])
    
    else:
        return(M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j+1]+M[i+1][j+1]+M[i+1][j]+M[i+1][j-1]+M[i][j-1])
        
        
#fonction pour déterminer l'évolution d'une case selon le nombre de voisins

def evol_cell(cell,nb):
    if cell == 0 and nb==3:
        return(1)
    
    if cell == 1:
        if nb == 2 or nb == 3:
            return(1)
        else:
            return(0)
    
    else:
        return(0)

#fonction qui affiche l'évolution de la matrice. Maintenant on a une liste des matrices

def evolution(Mo,Nt):
    L = [] #liste des matrices
    Mat = np.zeros((Nb,Nb))
    for i in range(Nb):
        for j in range(Nb):
            bool = Mo[i][j]
            Mat[i][j] = bool
    
    L.append(Mat)
    
    k = 0
    while k < Nt:
        
        n = np.zeros((Nb,Nb))
        for i in range(Nb):
            for j in range(Nb):
                cell = Mat[i][j]
                nb = nb_voisin(Mat,i,j)
                new_cell = evol_cell(cell,nb)
                n[i][j] = new_cell
        Mat = n
        L.append(Mat)
        k+=1
        
    return(L)
    
def indice(x):
    x = float(x)
    i = int(x/pas)
    return(i)

#paramètres de modélisation

Nt = 500
dt = 100 #dt en ms

#Initialisation de la matrice de départ

Matrix = np.zeros((Nb,Nb))



        


    
#affichage clean avec Tkinter
            



#on créé un quadrillage



index = 0
id_start = 0

paused = False
L = evolution(Matrix,Nt)
    


def clic(event):
    global Matrix
    x, y = event.x, event.y
    i, j = indice(y), indice(x)
    
    value = Matrix[i][j]
    if value == 1:
        Matrix[i][j] = 0
        can.itemconfig(my_dictio[i,j],fill='black')
    if value == 0:
        Matrix[i][j] = 1
        can.itemconfig(my_dictio[i,j],fill='white')
    
    
    
    
    
def anime_start():
    global paused, id_start,L
    paused = False
    if id_start == 0:
        L = evolution(Matrix,Nt)
        id_start += 1
        anime()
    else:
        anime()
    
def anime_stop():
    global paused
    paused = True

def anime_reset():
    global paused,index,L,id_start
    paused = True
    index = 0
    id_start = 0
    for i in range(Nb):
        for j in range(Nb):
            can.itemconfig(my_dictio[i,j],fill='white')
            Matrix[i][j] = 0

    
def generate():
    global paused,index,L,id_start
    for i in range(Nb):
        for j in range(Nb):
            rand = np.random.randint(0,2)
            if rand==0:
                can.itemconfig(my_dictio[i,j],fill='white')
                Matrix[i][j] = 0
            else:
                can.itemconfig(my_dictio[i,j],fill='black')
                Matrix[i,j] = 1

        
            

def anime():
    global index,paused,L

    if not paused:
        if index < Nt:
            matriz = L[index]
        
            for i in range(Nb):
                for j in range(Nb):
                
                    value = matriz[i][j]
                
                    if value == 1:
                        can.itemconfig(my_dictio[i,j],fill='black')
                
                    else:
                        can.itemconfig(my_dictio[i,j],fill='white')
            index += 1
            fen.after(dt,anime)

#quadrillage

fen = Tk()
can = Canvas(fen,bg='light gray',height = Cote,width = Cote)
can.pack()
        
for m in range(Nb+1):
    can.create_line(0,m*pas,Cote,m*pas,fill='black')
    can.create_line(m*pas,0,m*pas,Cote,fill='black')
    
    
#création d'un dictionnaire

my_dictio = {}

for i in range(Nb):
    for j in range(Nb):
        my_dictio[i,j] = "case"+str(i)+str(j)
        
#carrés blancs de base

for i in range(Nb):
    for j in range(Nb):
        my_dictio[i,j] = can.create_rectangle(j*pas,i*pas,(j+1)*pas,(i+1)*pas,fill='white',outline='black')

bouton_start = Button(fen,text="Start",command=anime_start)
bouton_stop = Button(fen,text="Stop",command=anime_stop)
bouton_reset = Button(fen,text="Reset",command=anime_reset)
bouton_gen = Button(fen,text="Random Generate",command=generate)


can.bind("<Button-1>", clic)
bouton_start.pack(side="bottom", fill='both', expand=True, padx=4, pady=4)
bouton_stop.pack(side="bottom", fill='both', expand=True, padx=5, pady=4)
bouton_reset.pack(side="bottom", fill='both', expand=True, padx=6, pady=4)
bouton_gen.pack(side="bottom", fill='both', expand=True, padx=7, pady=4)

fen.title('Conways Game of Life')
fen.mainloop()

