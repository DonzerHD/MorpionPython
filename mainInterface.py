import tkinter as tk
import tkinter.messagebox as messagebox

fenetre = tk.Tk()
fenetre.resizable(False,False)
fenetre.title("Morpion") 

signe = 'X'                                                     

def joueurClique(bouton: tk.Button) -> None:
    """
    Fonction appelée lorsque le joueur clique sur un bouton de la grille de jeu.
    
    Args:
        bouton (tk.Button): bouton de la grille de jeu sur lequel le joueur a cliqué.
    """
    global signe
    print(bouton)
    # vérifier si la case est vide
    if bouton["text"] == ' ':
         # mettre à jour la grille de jeu et le bouton
        bouton.config(text=signe)
        verification()
        egalite()
        # changer le signe
        if signe == 'X':
            bouton.config(text=signe, fg='red')
            signe = 'O'
        else:
            bouton.config(text=signe, fg='blue')
            signe = 'X'
    else:
        messagebox.showinfo("Case vide" , "La case n'est pas vide.")
    
        
        
def verification() -> None:
    """
    Vérifie si un joueur a gagné en parcourant les lignes colonnes et diagonales de la grille de jeu.
    Si un joueur a gagné affiche un message de victoire et termine le jeu.
    """
    #ligne
    for i in range(3):
        gagnerligne = True
        for j in range(3):
            bouton = fenetre.grid_slaves(row=i,column=j)
            if bouton[0].cget("text") != signe:
                gagnerligne = False   
                break
        if gagnerligne:
            messagebox.showinfo("Gagné", "Le joueur avec le signe " + signe + " a gagné!")
            exit()
    # colonne
    for i in range(3):
        gagnercolonne = True
        for j in range(3):
            bouton = fenetre.grid_slaves(row=j,column=i)
            if bouton[0].cget("text") != signe:
                gagnercolonne = False
                break  
        if gagnercolonne:
            messagebox.showinfo("Gagné", "Le joueur avec le signe " + signe + " a gagné!")
            exit()
          
     # les 2 diagonales   
    gagnerdiagonale = True
    for i in range(3):
        bouton = fenetre.grid_slaves(row=i,column=i)
        if bouton[0].cget("text") != signe:
            gagnerdiagonale = False
            break 
    if gagnerdiagonale:
        messagebox.showinfo("Gagné", "Le joueur avec le signe " + signe + " a gagné!")
        exit()

    gagnerdiagonaleInverse = True
    for i in range(3):
        bouton = fenetre.grid_slaves(row=i,column=2-i)
        if bouton[0].cget("text") != signe:
            gagnerdiagonaleInverse = False
            break 
    if gagnerdiagonaleInverse:
        messagebox.showinfo("Gagné", "Le joueur avec le signe " + signe + " a gagné!")
        exit()
  
    
def egalite() -> None:
    """
    Vérifie si le jeu n'a pas de gagnant.
    Si toutes les cases de la grille de jeu sont remplies sans qu'un joueur n'ait gagné affiche un message d'égalité et termine le jeu.
    """
     #egal
    compter = 0
    for i in range(3):
        for j in range(3):
            bouton = fenetre.grid_slaves(row=i,column=j)
            if bouton[0].cget("text") != " ":  
                compter += 1
    if compter == 9:
        messagebox.showinfo("Egalité", "Match nul")
        exit()
        

#Création de la grille pour l'interface graphique
for i in range(3):
    for j in range(3):
        bouton = tk.Button(fenetre, text = ' ', bg='white' ,font = ('Arial', 20), width = 4, height = 2)
        bouton.grid(row = i , column = j)
        bouton.config(command=lambda bouton=bouton: joueurClique(bouton))
        

fenetre.mainloop()
