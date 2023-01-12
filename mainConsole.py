grille_morpion = [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]


def grille():
  """
  Fonction qui affiche l'état actuel de la grille de jeu à l'écran.
  
  """
  print("  1 2 3")
  for i, ligne in enumerate(grille_morpion):
    print(i+1, end=' ')
    print('|'.join(ligne))
 
   
def joueurSaisie(signe:str):
    """
    Demande à l'utilisateur de saisir la ligne et la colonne où il souhaite placer son symbole et vérifie si l'emplacement est valide et met à jour la grille de jeu.

    Args:
    signe (str): Le symbole que le joueur souhaite placer 'O' ou 'X'.

    Raises:
    ValueError: Si l'utilisateur entre autre chose qu'un chiffre pour la ligne ou la colonne.
    IndexError: Si l'utilisateur entre un chiffre en dehors des valeurs autorisées (1,2 et 3) pour la ligne ou la colonne.
    """
    try:
        ligne = int(input("Saisissez la ligne 1 ou 2 ou 3 où vous voulez jouer: ")) - 1
        colonne = int(input("Saisissez la colonne 1 ou 2 ou 3 où vous voulez jouer: ")) - 1
        if grille_morpion[ligne][colonne] != ' ':
         print('case déja pris')
         joueurSaisie(signe)
        else:
         grille_morpion[ligne][colonne] = signe
    except ValueError:
           print("Seulement les chiffres autorisés")
           joueurSaisie(signe)
    except IndexError:
           print("Seulement les chiffres 1,2 et 3 autorisées")
           joueurSaisie(signe)

     
            
def verification(signe:str) -> bool:
  """
  Vérifie si le symbole passé en argument a gagné en vérifiant s'il y a trois des mêmes symboles alignés dans une ligne colonne ou diagonale sur la grille de jeu.

  Args:
  signe (str): Le symbole 'O' ou 'X' qui doit être vérifié.

  Returns:
  bool: True si le symbole passé en argument a gagné False si aucun joueur n'a gagné.
  """
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

def egalite() -> bool:
  """
    Vérifie si la partie s'est terminée par un match nul en vérifiant si tous les emplacements sur la grille de jeu sont occupés.

    Returns:
    bool: True si la partie est nulle (tous les emplacements sont occupés) ou False sinon.
  """
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
       
