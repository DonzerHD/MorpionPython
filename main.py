grille_morpion = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]



def grille():
  print("  1 2 3")
  for i, ligne in enumerate(grille_morpion):
    print(i+1, end=' ')
    print('|'.join(ligne))
 
   
def joueurSaisie(signe):
     ligne = int(input("Saisissez la ligne 1 ou 2 ou 3 où vous voulez jouer: ")) - 1
     colonne = int(input("Saisissez la colonne 1 ou 2 ou 3 où vous voulez jouer: ")) - 1
     if grille_morpion[ligne][colonne] != ' ':
         print('case déja pris')
     else:
         grille_morpion[ligne][colonne] = signe

    
def verification(signe):
   #ligne
   for ligne in grille_morpion:
     if ligne == [signe , signe , signe]:
       return True
     #colonne
   for colonne in range(3):
     if grille_morpion[0][colonne] == signe and grille_morpion[1][colonne] and grille_morpion[2][colonne]:
       return True
     #diagonale
   
     
     
     



grille()
