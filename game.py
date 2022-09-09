import os
import time
from random import randint
from datetime import datetime
import pygame 
''' =======================================================================> '''

pygame.init()

def welcome_Game():

    
    
    


  art = '''

                              _____                      _______               
                              / ____|                    |___  (_)              
                              | |  __  __ _ _ __ ___   ___   / / _ _______ _ __  
                              | | |_ |/ _` | '_ ` _ \ / _ \ / / | |_  / _ \ '_ \ 
                              | |__| | (_| | | | | | |  __// /__| |/ /  __/ | | |
                              \_____|\__,_|_| |_| |_|\___/_____|_/___\___|_| |_|

                                          Developper Par Sami ABDULHALIM
                                          Developper Par Jeanne BISSINGA



    '''

  print(art)
  print() 
  entrer = input("voulez vous enter dans le jeu si oui taper 'oui'  : ")

  if entrer=="oui":
    os.system('clear')
    Menu()

  if entrer !="oui":
    os.system('clear')
    print("au revoir vous avez quitter le jeu  ")
    Quitter()  


      
  ''' =======================================================================> '''
  ''' colors variables  '''
bleu = '\033[94m'
OKGREEN = '\033[92m'
FAIL = '\033[91m'
  ''' =======================================================================> '''

  ''' function de Devinette (jeu)  '''

def Deviner(nb):
  nombre = 55

  if nb != nombre:
    print(f" {FAIL} perdu")
    time.sleep(2)
    os.system('clear')
    Menu()
  elif nb == nombre:
    print(f"{OKGREEN} gagner")



    
''' =======================================================================> '''


''' Menu '''

def Menu():
  print("Menu Principal ")
  print("1.cree une nouvelle partie ")
  print("2. A propos  ")
  print("3. Quitter le Jeu ")
  Choix = int(input("taper le numero de votre choix : "))
    
  if Choix == 1:
    os.system('clear')
    Start_game()

  elif Choix == 2:
    os.system('clear')
    About()

    

  elif Choix == 3:
    Quitter()

      

''' =======================================================================> '''





''' retourner au Menu principal dans le jeu   '''
def RetourMenu():
  Retour = input("voulez vous retourner au Menu principal ? Si oui taper `oui` ")

  if Retour =='oui':
    os.system('clear')
    Menu()
      
  else:
    return False  



''' =======================================================================> '''



''' function a propos du jeu  '''

def About(): 
  os.system('clear')
  date = datetime.now()
  print("le jeu a ete cree en 2020 par -----[SAMI ABDULHALIM]--------[JEANNE BISSINGA]------------- ")
  print("")
  print(f"le jeu est a jour : {date} ")
  time.sleep(3)
  RetourMenu()
    



''' =======================================================================> '''





''' function quitter le jeu  '''
def Quitter():
  os.system('clear')
  print("vous allez quitter le jeu .... ")
  time.sleep(3)
  exit()
    

''' =======================================================================> '''



''' commencer le jeu  '''


def Start_game():
  ''' demander le non du joueur  '''
  Name_player = input("comment on peut vous appeller ? ")
  os.system('clear')
  time.sleep(1.5)
  print(f"{bleu} bienvenue dans le Jeu GameZIZEN {Name_player}")

  print("Nous allons jouer un petit jeu de Devinette pour confirmer que vous n'etes pas un robot ")
  print("Vous devez deviner le nombre entré dans le programme. S'il est valide vous gagnez et vous rentrez dans le jeu, sinon vous perdez. PS: le nombre est : 55  ")
    
  Deviner(int(input("entrer une valuer : ")))
  time.sleep(4)
  os.system("clear")
  print(f"Vous êtes maintenant chez vous  {Name_player} où voulez vous aller ?  :")
  position ()


i = 1
while i <= 4 :

  O = "False"
  def position ():
    print("1. aller au lac pour chercher des armes ")
    print("2. aller à la forêt pour combattre le montre")
    Ask_Depart = input("où voulez vous aller ? : ")


    if Ask_Depart == '1':
      os.system("clear")
      GameLac()  
      
    elif Ask_Depart == "2":
      O = "True" #pour dire que l'inventaire contient au moins un objet
      os.system("clear")
      GameForet()
      

    if not Ask_Depart:
      print(f" {FAIL} Vous n'avez rien entré {Name_player} ")
      
    elif Ask_Depart != "1" or Ask_Depart != "2":
      print(f" {FAIL} Désolé je n'ai pas compris votre demande  ")



  ''' =======================================================================> '''

  inventaire = {
          "Ak47" : 0 , 
          "couteau" : 0,
          "AWP" : 0,
          "P50" : 0,
          "M47" :0,
          "RpG" : 0
      }

  def objet() :
    D =  randint(1, 6)

    if D == 1 :
      print("vous avez trouver : Ak47")
      print(f"On vas stocker votre arme  dans votre inventaire. ")
      inventaire ["Ak47"] = inventaire ["Ak47"] + 1
    elif D == 2 :
      print("vous avez trouver :  un couteau ")
      print(f"On vas stocker votre arme  dans votre inventaire. ")
      inventaire ["couteau"] = inventaire ["couteau"] + 1
    elif D == 3 :
      print("vous avez trouver : AWP ")
      print(f"On vas stocker votre arme  dans votre inventaire. ")
      inventaire ["AWP"] = inventaire ["AWP"] + 1
    elif D == 4 :
      print("vous avez trouver :  P50")
      print(f"On vas stocker votre arme  dans votre inventaire. ")
      inventaire ["P50"] = inventaire ["P50"] + 1
    elif D == 5 :
      print("vous avez trouver : M47")
      print(f"On vas stocker votre arme  dans votre inventaire. ")
      inventaire ["M47"] = inventaire ["M47"] + 1
    elif D == 6 :
      print("vous avez trouver : RPG")
      print(f"On vas stocker votre arme  dans votre inventaire. ")
      inventaire ["RpG"] = inventaire ["RpG"] + 1
    return inventaire
        
    
  ''' =======================================================================> '''



  ''' function Monstre '''
    
  def monstre():
    print("un Monstre vient d'appraitre !!!!!")
    pygame.mixer.music.load("Wolf Howl.mp3")  
    pygame.mixer.music.play()
    return (f"votre inventaire contient : {inventaire}") 

    if not O :

      print("Votre liste est vide pour l'instant ")
      print("")
      print("Vous ne pouvez pas combattre le monstre")
      print("")
      print("Aller chercher des armes ")
      time.sleep(8)
      os.system("clear")
      Start_game()
            
    else : 
      print ("Vous voulez combatre avec:")
      print (" 1.Ak47 \n 2.couteau \n 3.AWP \n 4.P50 \n 5.M47 \n 6.RpG" )
      print ("Faite votre choix :")
      choice = int (input ())
      #combat()
    return choice

  choix = montre ()
  if choix == 1 :
    print("VOUS  avez toucher le monstre avec une AK47 ")
    print("la santé de Monstre est =  ")
    print(Monstre_Sante - AK47_dommage)

  elif choix == 2 :
    print("VOUS  avez toucher le monstre avec une couteau ")
    print("la santé de Monstre est = ")
    print(Monstre_Sante - Couteau_dommage)

  elif choix == 3 :
    print("VOUS  avez toucher le monstre avec une AWP")
    print("la santé de Monstre est = ")
    print(Monstre_Sante - AWP_dommage)

  elif choix == 4 :
    print("VOUS  avez toucher le monstre avec une P50")
    print("la santé de Monstre est = ")
    print(Monstre_Sante - P50_dommage)   

  elif choix == 5 :
    print("VOUS  avez toucher le monstre avec une M47")
    print("la santé de Monstre est = ")
    print(Monstre_Sante - M47_dommage)
            
  elif choix == RpG:
    print("VOUS  avez toucher le monstre avec une P50")
    print("la santé de Monstre est = ")
    print(Monstre_Sante - RpG_dommage)
                  
            

      #print("")
      #Ask_combat = input(" etes vous pret pour commencer le combat ? oui/non :  ")

      #if Ask_combat == "oui":
            #combat()
      
      #else:
          # Quitter()
          
      
  ''' =======================================================================> '''
    
  ''' function attaque '''

  Monstre_Sante = 50
  Joueur_Sante = 30

  def De () :
    return (randint (1,6))

  def montre_attac () :
    DeMontre = De ()
    if DeMontre == 1 :
      Joueur_Sante = Joueur_Sante - 15
    elif DeMontre == 2 :
      Joueur_Sante = Joueur_Sante - 30
    elif DeMontre == 3 :
      Joueur_Sante = Joueur_Sante - 15
    elif DeMontre == 4 :
      Joueur_Sante = Joueur_Sante - 25
    elif DeMontre == 5 :
      Joueur_Sante = Joueur_Sante - 5
    elif DeMontre == 6 :
      Joueur_Sante = Joueur_Sante - 10
    return Joueur_Sante
    

  #armes dommages :
  #AK47_dommage = 30
  #M47_dommage = 20
  #RPG_dommage = 60
  #P50_dommage = 40
  #AWP_dommage = 46
  #Couteau_dommage = 15

  def joueur_attac () :
    if C == 1 :
      Montre_Sante = Montre_Sante - 30
    elif C == 2 :
      Montre_Sante = Montre_Sante - 15
    elif C == 3 :
      Montre_Sante = Montre_Sante - 46
    elif C == 4 :
      Montre_Sante = Montre_Sante - 40
    elif C == 5 :
      Montre_Sante = Montre_Sante - 20
    elif C == 6 :
      Montre_Sante = Montre_Sante - 60
    return Montre_Sante

  ''' =======================================================================> '''
    
  ''' function combat joueur vs monstre '''

  def combat () :
    montre_attac ()
    joueur_attac ()

  JS = montre_attac () # JS ( joueur santé)
  if JS <= 0 :
    print ("Game over!!!")
  else :
    print("Le monstre n'est pas encore mort ressayer .....")
    time.sleep(5)
    GameLac()


  MS = joueur_attac () # MS (montre santé)
  if MS <= 0 :
    print ("Bravo vous avez battu le montre! Vous allez passez au niveau ", i )
  

  if i == 2 :
    Joueur_Sante = Joueur_Sante + 10
    Montre_Sante = Montre_Sante + 10
    inventaire [P50] = inventaire [P50] + 5
  elif i == 3 :
    Joueur_Sante = Joueur_Sante + 15
    Montre_Sante = Montre_Sante + 15
    inventaire [AWP] = inventaire [AWP] + 5
  elif i == 4 :
    Joueur_Sante = Joueur_Sante + 20
    Montre_Sante = Montre_Sante + 20
    inventaire [M47] = inventaire [M47] + 2
    inventaire [P50] = inventaire [P50] + 5
  elif i == 5 :
    Joueur_Sante = Joueur_Sante + 25
    Montre_Sante = Montre_Sante + 25
    inventaire [Couteau] = inventaire [Couteau] + 5
    inventaire [RPG] = inventaire [RPG] + 5

    #def combat():
          #print("Combat Start ")
          #time.sleep(3)
          #os.system("clear")

          #for k in inventaire :
          
          




    ''' =======================================================================> '''



  def GameLac():
    print("trajet en cour ....")
    pygame.mixer.music.load("lac.mp3")
    pygame.mixer.music.play()
    time.sleep(3.5)
    os.system('clear')
    print("vous etes arriver au lac  ")

    objet()
    print("")
    joinForet = input("voulez-vous aller au foret ? : ")

    if joinForet == "oui":      
      print("vous allez rejoindre la foret maintenant")
      time.sleep(8)
      os.system("clear")
      GameForet()
      

    ''' =======================================================================> '''

    

  def GameForet():
    print("trajet en cour ....")
    time.sleep(3.5)
    os.system('clear')
    print("vous etes arriver au foret ")
    C = monstre()

    if C == 1 :
      inventaire ["AK47"] = inventaire ["AK47"] - 1
    elif C == 2 :
      inventaire ["couteau"] = inventaire ["couteau"] - 1
    elif C == 3 :
      inventaire ["AWP"] = inventaire ["AWP"] - 1
    elif C == 4 :
      inventaire ["P50"] = inventaire ["P50"] - 1
    elif C == 5 :
      inventaire ["M47"] = inventaire ["M47"] - 1
    elif C == 6 :
      inventaire ["RpG"] = inventaire ["RpG"] - 1


  i += 1

  ''' =======================================================================> '''

welcome_Game()


