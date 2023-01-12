from tkinter import *

fenetre = Tk()
fenetre.geometry('400x400')
fenetre.title('Tkinter tutoriel')
fenetre['bg'] = 'red'
fenetre.resizable(height=False,width=False)

mon_menu = Menu(fenetre)

def jouerMorpion():
    print('tu as cliqué morpion')

def jouerPuissance4():
    print('tu as cliqué sur Puissance4')


#Sous onglet Morpion

morpion = Menu(mon_menu, tearoff=0)
morpion.add_command(label="Contre Joueur", command=jouerMorpion)
morpion.add_command(label="Contre IA")

#Sous onglet Puissance4

puissance4 = Menu(mon_menu, tearoff=0)
puissance4.add_command(label="Contre Joueur", command=jouerPuissance4)
puissance4.add_command(label="Contre IA")

#Les 2 principaux onglets
mon_menu.add_cascade(label="Morpion", menu=morpion)
mon_menu.add_cascade(label="Puissance 4", menu=puissance4)

fenetre.config(menu=mon_menu)

fenetre.mainloop()


     
      
     
