grille_morpion = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]



def grille():
  for ligne in grille_morpion:
    print('|'.join(ligne))
 
   
def joueur(signe):
     ligne = int(input("Saisissez la ligne 1 ou 2 ou 3 où vous voulez jouer: ")) - 1
     colonne = int(input("Saisissez la colonne 1 ou 2 ou 3 où vous voulez jouer: ")) - 1
     if grille_morpion[ligne][colonne] != ' ':
         print('case déja pris')
     else:
         grille_morpion[ligne][colonne] = signe

    
def jouer(signe):
   for ligne in grille_morpion:
     if ligne == [signe , signe , signe]:
       return True
     
     
     



grille()
