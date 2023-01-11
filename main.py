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
         joueurSaisie(signe)
     else:
         grille_morpion[ligne][colonne] = signe
            
def verification(signe):
  #ligne
  for ligne in grille_morpion:
    if ligne == [signe , signe , signe]:
        return True     
     #colonne
  for colonne in range(3):
     if grille_morpion[0][colonne] == signe and grille_morpion[1][colonne] == signe and grille_morpion[2][colonne] == signe:
      return True
     
     #diagonale
  if  grille_morpion[0][0] == signe and grille_morpion[1][1] == signe and grille_morpion[2][2] == signe:
    return True
  if  grille_morpion[0][2] == signe and grille_morpion[1][1] == signe and grille_morpion[2][0] == signe:
    return True
  return False

def egalite():
  grille_pleine = True
  for ligne in grille_morpion:
    if ' ' in ligne:
      grille_pleine = False
      break
  if grille_pleine:
    return True
  return False

while True: 
  grille()
  joueurSaisie('O')
  if verification('O') == True:
    grille()
    print('O a gagné')
    break
  if egalite() == True:
    grille()
    print('match nul')
    break
  grille()
  joueurSaisie('X')
  if verification('X') == True:
    grille()
    print('X a gagné')
    break
  if egalite() == True:
    grille()
    print('match nul')
       
