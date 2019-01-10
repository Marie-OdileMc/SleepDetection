
# # AFFICHE CARRE VERT AU CLIC
# from tkinter import *

# def Clic(event):
#     """ Gestion de l'événement Clic gauche sur la zone graphique """
#     # position du pointeur de la souris
#     X = event.x
#     Y = event.y
#     # on dessine un carré
#     r = 20
#     myrect = Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='black',fill='green')


# def Effacer():
#     """ Efface la zone graphique """
#     Canevas.delete(ALL)

# def EffacerRect(event):
#     """ Efface un carré """
#     X = event.x
#     Y = event.y
#     Canevas.delete(myrect)

# # Création de la fenêtre principale
# Mafenetre = Tk()
# Mafenetre.title('Carrés')

# # Création d'un widget Canvas
# Largeur = 480
# Hauteur = 320
# Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
# # La méthode bind() permet de lier un événement avec une fonction :
# # un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur Clic()
# Canevas.bind('<Button-1>', Clic)
# Canevas.bind('<Button-3>', EffacerRect)
# Canevas.pack(padx =5, pady =5)

# # Création d'un widget Button (bouton Effacer)
# Button(Mafenetre, text ='Effacer', command = Effacer).pack(side=LEFT,padx = 5,pady = 5)

# # Création d'un widget Button (bouton Quitter)
# Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

# Mafenetre.mainloop()


# ####### EFFACER UNE FORME
# from tkinter import *
# import random
# import time

# start = time.time()
# # run your code


# def Effacer():
#     """ Efface la zone graphique """
#     Canevas.delete(ALL)

# def EffacerRect(event):
#     """ Efface un carré """
#     X = event.x
#     Y = event.y
#     Canevas.delete(myrect)

# # Création de la fenêtre principale
# Mafenetre = Tk()
# Mafenetre.title('Carrés')

# # Création d'un widget Canvas
# Largeur = 480
# Hauteur = 320
# Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')

# # on dessine un carré
# X = random.randint(0,Largeur)
# Y = random.randint(0,Hauteur)
# r = 20
# myrect = Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='green',fill='green')
# Canevas.bind('<Button-1>', EffacerRect)
# end = time.time()
# elapsed = end - start
# print (elapsed)
# Canevas.pack(padx =5, pady =5)

# # Création d'un widget Button (bouton Effacer)
# Button(Mafenetre, text ='Effacer', command = Effacer).pack(side=LEFT,padx = 5,pady = 5)

# # Création d'un widget Button (bouton Quitter)
# Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

# Mafenetre.mainloop()



####### FINAL CODE
from tkinter import *
import random
import threading
import time


### MAIN
# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Fatigue')

label = Label(Mafenetre, text="Cliquez aussi vite que possible quand le rectangle devient VERT")
label.pack()


# Création d'un widget Canvas
Largeur = 400
Hauteur = 320
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')

### FONCTIONS
def ChangeColor ():
    # change de couleur au bout de 5 à 9sec
    #print ("Changement de couleur")
    Canevas.itemconfigure(myrect, fill='green')  
    #Détecte clic de la souris
    Canevas.bind('<Button-1>', Clic)

def Clic(event):
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    #On indique clic de la souris
    #print ("Clic de la souris !")
    done = time.time()
    elapsed = done - start
    print(elapsed-t)
    if elapsed-t > 0.3:
        label = Label(Mafenetre, text="Tu es fatigué :( EVITER DE CONDUIRE")
        label.pack()
    else :
        label = Label(Mafenetre, text="Tu peux conduire :)")
        label.pack()






# on dessine un rectangle rouge
myrect = Canevas.create_rectangle(100, 100, 300, 250, outline='red',fill='red')
Canevas.pack(padx =5, pady =5)

# Commencer >> lance le test
t = random.randint(5,9)
Button(Mafenetre, text ='Commencer', command = threading.Timer(t, ChangeColor).start()).pack(side=LEFT,padx = 5,pady = 5)
start = time.time()
#print("Début du chrono")

# Quitter >> ferme la fenêtre
Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

Mafenetre.mainloop()


