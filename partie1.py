"""Auteur : Versweyveld Théo
   Matricule : 483062
   Section : Sciences informatiques BAC 1
   Titre : Partie 1, projet Slideways.
"""
# CONSTANTES

NB_LIGNES = int(4)
NB_COLONNES = int(4)
NB_ALIGNES_GAGNANT = int(4)
NB_JOUEURS = int(2)
VIDE = 0 ; ROUGE = 1 ; JAUNE = 2
SYMBOLE_COULEUR = (" ","X","O") # tuple correspondant aux 3 couleurs ci-dessus

class Joueur :
    def __init__(self, inCouleur , inNom=""): #self signifie 'joueur'
        self.inCouleur = int(inCouleur)
        self.nom = str (inNom)
        self.Joueur_2 = bool(inNom==" ")
        if inNom == " "
            self.nom = "Joueur_2"
        self.nb_victoires = int(0)
class game :
    def __init__(self, inNomPlayer1 , inNomPlayer2 = ""):
        self.grille = [[0 for i in range(NB_COLONNES )] for j in range(NB_LIGNES )]
        Player1 = Joueur(ROUGE, inNomPlayer1)
        Player2 = Joueur(JAUNE, inNomPlayer2)
        self.players = (Player1, Player2)
        self.lvl = 1
    #méthode affichant la grille
    def show_grille(self): #OK
        print(1) # sauter une ligne
        for i in range(NB_LIGNES) :
            print("  - - - -",end=" ")
            for j in range(NB_COLONNES) :
                 print(self.symbole_case(self.grille[i][j]), end=" ")
            print(" ")
        self.afficher_numeros_colonnes()
    #méthode nécessaire à l'affiche de la grille
    def symbole_case(self,inCouleur) : #OK
       return SYMBOLE_COULEUR[inCouleur]
    #méthode affichant les numéros des différentes colonnes
    def afficher_numeros_colonnes(self) : #OK
        print(" ",end=" ") # espace pour le bord droit
        for j in range(1) :
            print("A B C D" ,end=" ")
        print(" ") # pour aller à la Ligne
    #méthode qui test s'il y a un gagnant ou s'il y a match null, elle renvoie le gagnant si nécessaire
    def afficher_nom_rangée(self):
        for i in range(NB_LIGNES):
            print(" 1 2 3 4", end=" ")
        print(" ")


    def test_if_win(self):
        res = False
        who_win = ""
        #teste si toutes les cases de la grille sont remplies, si c'est le cas alors > partie nulle
        sum = 0
        for i in range(NB_LIGNES):
            for j in range(NB_COLONNES):
                if self.grille[i][j] != 0:
                    sum += 1
        sum_dim_mat = NB_LIGNES * NB_COLONNES
        #si toutes les cases de la grilles sont remplies ça veut dire qu'il n'y a plus de 0 dans la matrice et donc qu'il y autant d'élément différent de 0 que de place dans la grille
        if sum == sum_dim_mat:
            res = True
        #test s'il y a 4 pions à l'horizontale
        for i in range(NB_LIGNES): #OK
            for j in range(NB_COLONNES - 3):
                if self.grille[i][j] == 1:
                    if self.grille[i][j] == self.grille[i][j+1] and self.grille[i][j+1] == self.grille[i][j+2] and self.grille[i][j+2] == self.grille[i][j+3]:
                        res = True
                        who_win = "Joueur_1"
                if self.grille[i][j]  == 2:
                    if self.grille[i][j] == self.grille[i][j+1] and self.grille[i][j+1] == self.grille[i][j+2] and self.grille[i][j+2] == self.grille[i][j+3]:
                        res = True
                        who_win = "Joueur_2"
        #test s'il y a 4 pions à la verticale
        for i in range(NB_LIGNES-3): #OK
            for j in range(NB_COLONNES):
                if self.grille[i][j] == 1:
                    if self.grille[i][j] == self.grille[i+1][j] and self.grille[i+1][j] == self.grille[i+2][j] and self.grille[i+2][j] == self.grille[i+3][j]:
                        res = True
                        who_win = "Joueur_1"
                if self.grille[i][j]  == 2:
                    if self.grille[i][j] == self.grille[i+1][j] and self.grille[i+1][j] == self.grille[i+2][j] and self.grille[i+2][j] == self.grille[i+3][j]:
                        res = True
                        who_win = "Joueur_2"
        #faire idem pour la diagonnale droite
        for i in range(NB_LIGNES-3):
            for j in range(NB_COLONNES -3):
                if self.grille[i][j] == 1:
                    if self.grille[i][j] == self.grille[i+1][j+1] and self.grille[i+1][j+1] == self.grille[i+2][j+2] and self.grille[i+2][j+2] == self.grille[i+3][j+3]:
                        res = True
                        who_win = "Joueur_1"
                if self.grille[i][j] == 2:
                    if self.grille[i][j] == self.grille[i+1][j+1] and self.grille[i+1][j+1] == self.grille[i+2][j+2] and self.grille[i+2][j+2] == self.grille[i+3][j+3]:
                        res = True
                        who_win = "Joueur_2"

        #faire idem pour la diagonnale gauche
        for i in range(3,NB_LIGNES):
            for j in range(3,NB_COLONNES):
                if self.grille[i][j] == 1:
                    if self.grille[i][j] == self.grille[i-1][j-1] and self.grille[i-1][j-1] == self.grille[i-2][j-2] and self.grille[i-2][j-2] == self.grille[i-3][j-3]:
                        res = True
                        who_win = "Joueur_1"
                if self.grille[i][j] == 2:
                    if self.grille[i][j] == self.grille[i-1][j-1] and self.grille[i-1][j-1] == self.grille[i-2][j-2] and self.grille[i-2][j-2] == self.grille[i-3][j-3]:
                        res = True
                        who_win = "Joueur_2"

        return res, who_win

    #cette méthode va vérifier s'il est possible d'ajouter un pio dans la colonne choisie
    def test_si_choix_valide(self,choice): #OK
        res = False
        ligne_ou_ajout = NB_LIGNES-1
        choice -= 1
        #ici on va vérifier si la dernière ligne est libre, si pas on ajoute à la ligne d'au dessus et ainsi de suite
        stop = False
        while stop == False:
            if ligne_ou_ajout < 0:
                stop = True
                res = False
            else:
                if self.grille[ligne_ou_ajout][choice] == 0:
                    stop = True
                    res = True
                else:
                    ligne_ou_ajout -= 1
        return res

    #méthode qui gère l'ajout de pion dans la grille quand c'est le tour du joueur
    def add_elem_in_grille_Joueur_1(self,choice): #OK
        ligne_ou_ajout = NB_LIGNES-1 #on suppose qu'on ajoute le "pion" à la dernière ligne
        choice -= 1
        #ici on va vérifier si la dernière ligne est libre, si pas on ajoute à la ligne d'au dessus et ainsi de suite
        stop = False
        while stop == False:
                if self.grille[ligne_ou_ajout][choice] == 0:
                    self.grille[ligne_ou_ajout][choice] = 1
                    stop = True
                else:
                    ligne_ou_ajout -= 1

    #méthode qui gère l'ajout de pion dans la grille quand c'est le tour de l'IA
    def add_elem_in_grille_Joueur_2(self,choice):
        ligne_ou_ajout = NB_LIGNES - 1  # on suppose qu'on ajoute le "pion" à la dernière ligne
        choice -= 1
        # ici on va vérifier si la dernière ligne est libre, si pas on ajoute à la ligne d'au dessus et ainsi de suite
        stop = False
        while stop == False:
            if self.grille[ligne_ou_ajout][choice] == 0:
                self.grille[ligne_ou_ajout][choice] = 1
                stop = True
            else:
                ligne_ou_ajout -= 1


#fonction permettant au joueur de choisir la colonne et vérifie si c'est possible
def choose_colonne(inJeu): #OK
    choice = int(input("Joueur_1 : Dans quelle colonne souhaitez-vous jouer ? "))
    while choice < 1 or choice > NB_COLONNES:
        choice = int(input("Joueur_2 : Dans quelle colonne souhaitez-vous jouer ? "))
    #vérifie que le choix de la colonne est bien valide
    val_choix = inJeu.test_si_choix_valide(choice)
    while val_choix != True:
        choice = choose_colonne()
        val_choix = inJeu.test_si_choix_valide(choice)
    return choice

def main(): #FONCTION PRINCIPALE QUI APPELLE LES DIFFERENTES FONCTION ET METHODE DE LA CLASSE game
    print("Bienvenue au Slideways")
    inJeu = game("Théo") #crée une partie avec le nom de joueur Théo
    end_game = False
    inJeu.show_grille()
    while end_game == False:
        choix = choose_colonne(inJeu)
        inJeu.add_elem_in_grille_Joueur_1(choix)
        inJeu.add_elem_in_grille_Joueur_2(choix)
        inJeu.show_grille()
        end_game, winner = inJeu.test_if_win()

    if winner == "Joueur_1":
        print("Félicitations, Joueur_1 a gagné la partie !")
    if winner == "Joueur_2":
        print("Félicitations, Joueur_2 a gagné la partie ! ")
    if winner == "":
        print("Partie nulle")


if __name__ == '__main__':
    main()





