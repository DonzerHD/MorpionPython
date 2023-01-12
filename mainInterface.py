import tkinter as tk

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
        # changer le signe
        if signe == 'X':
            signe = 'O'
        else:
            signe = 'X'
    else:
        print("La case n'est pas vide.")
        
def verification():
   pass

def egalite() -> bool:
   pass
        

#Création de la grille pour l'interface graphique
for i in range(3):
    for j in range(3):
        button = tk.Button(fenetre, text = ' ', font = ('Arial', 20), width = 4, height = 2)
        button.grid(row = i , column = j)
        button.config(command=lambda button=button: joueurClique(button))

fenetre.mainloop()
