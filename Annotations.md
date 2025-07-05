# Notes d'exploration des fichiers du projet

## Structure des fichiers clés 

- **syntax.py** :  Définit la structure grammaticale du langage Pithon. 
Chaque élément du langage a sa propre représentation.

- **envvalue.py** : Contient les représentations des valeurs manipulées à l'exécution par l'interpréteur.

- **primitive.py** : Définit les fonctions primitives de base (opérations arithmétiques, opérations de comparaison et fonctions utilitaires) 
Ces fonctions manipulent les valeurs définies dans envvalue.py

- **envframe.py** : Regroupe les mécanismes liés à la portées d'exécution, comme le stockage des variables, 
la création de portées pour les fonctions et la gestion des objets (instances de classes).
Ce module contient les structures internes qui encadrent le comportement du langage.

Lorsqu'un nouvel environnement est créé, la méthode '__init__' initialise : 
- un dictionnaire 'vars' qui stocke les variables locales
- une référence optionnelle vers un environnement parent, utilisée pour retrouver des variables dans des portées supérieures
si elle ne sont pas trouvées localement

- **evaluator.py** : Analyse chaque noeud syntaxique et applique la logique appropriée pour l'évaluer,
reproduisant le comportement attendu du langage Python (ou presque). 
C'est ici que les expressions sont résolues, les instructions exécutées et les valeurs manipulées.