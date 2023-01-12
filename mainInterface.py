import tkinter as tk
import tkinter.messagebox as messagebox

fenetre = tk.Tk()
fenetre.resizable(False,False)
fenetre.title("Morpion")

signe = 'X'


def joueurClique(bouton):
    global signe
    print(bouton)
    # vérifier si la case est vide
    if bouton["text"] == ' ':
         # mettre à jour la grille de jeu et le bouton
        bouton.config(text=signe)
        verification()
        # changer le signe
        if signe == 'X':
            signe = 'O'
        else:
            signe = 'X'
    else:
        messagebox.showinfo("Case vide" , "La case n'est pas vide.")
    
        
        
def verification():
    #ligne
    for i in range(3):
        gagner = True
        for j in range(3):
            bouton = fenetre.grid_slaves(row=i,column=j)
            if bouton[0].cget("text") != signe:
                gagner = False   
        if gagner:
            messagebox.showinfo("Gagné", "Le joueur avec le signe " + signe + " a gagné!")
            exit()
    
def egalite():
   pass
        

#Création de la grille pour l'interface graphique
for i in range(3):
    for j in range(3):
        bouton = tk.Button(fenetre, text = ' ', font = ('Arial', 20), width = 4, height = 2)
        bouton.grid(row = i , column = j)
        bouton.config(command=lambda bouton=bouton: joueurClique(bouton))
        

fenetre.mainloop()
