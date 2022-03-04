```
Fonction Jeu.lancer
    Tant que plus_de_2_joueurs
        
        joueurs = determiner_ordre_joueurs()

        calculer_actions_possibles()

        joueur[0].lancer_des()

        Ecrire "Choisissez une action"
        Ecrire joueur_actuel.actions_autorisees
        Tant que nom_action pas dans joueur_actuel.actions_autorisees
                Lire nom_action 
            
        action_precedente = joueur_actuel.action(nom_action)
           
        Pour i allant de 1 à nb_joueurs-1
            joueur[i].lancer_des()

            Ecrire "Choisissez une action"
            Ecrire joueur_actuel.actions_autorisees
            
            Tant que nom_action pas dans joueur_actuel.actions_autorisees
                Lire nom_action 
            
            action_precedente = joueur_actuel.action(nom_action, action_precedente)


        joueurs, nb_joueurs = eliminer_joueurs()
```