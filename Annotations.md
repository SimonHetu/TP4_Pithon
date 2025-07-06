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

**PiClassDef** représente la déclaration d'une classe c'est la structure grammaticale qui permet d'introduire une nouvelle classe dans le langage. Lorsqu'il est évalué, il produit une valeur de type VClassDef, stockée dans l'environnement qui contient : 
- le nom de la classe
- un dictionnaire de méthodes sous forme de VFunctionClosure associées à leur environnement de définition

**PiFunctionCall** dans le language Python (et donc dans Pithon) appeler une classe est aussi un appel de fonction. Lorsqu'on appelle une classe on déclenche en fait un mécanisme spéciale qui:
- Crée un objet comme instance de la classe (VObject)
- Cherche une méthode  spéciale __init__ dans la classe
Si elle existe :
- Crée un VMethodClosure pour lier cette méthode à l’instance (équivalent du self)
- Prépare un environnement d’appel (EnvFrame) avec :
    - self pointant vers l’objet
    - les autres arguments positionnels associés à leurs noms
    - une liste (VList) pour les arguments restants si *args est utilisé
    - Évalue chaque instruction dans le corps de la méthode __init__
Finalement, retourne l’objet instancié

**PiAttribute** et **PiAttributeAssignment**
Permettent d'accèder aux attributs d'un objet et d'en assigner de nouveaux.
**PiAttribute** - Accès à un attribut
- Évalue l'objet
- Lève une erreur si ce n'est pas un VObject
- Si l'attribut est dans obj.attributes retourne sa valeur
- Sinon, cherche une méthode du même nom dans obj.class_def.methods
    - Si trouvée retourne une VMethodClosure(méthode liée à l'objet)
    - Sinon lève une erreur d'attribut
**PiAttributeAssignment** - Assignation d'un attribut
- Évalue l'objet cible et la valeur à assigner
- Vérifie que l'objet est un VObject, sinon lève une erreur de type
- Insère l'attribut dans le dictionnaire de l'objet (obj.attributes)
- Retourne la valeur assignée

**VMethodClosure**

Représente une méthode liée à une instance d'objet (similaire à self method() en Python)

Lorsqu'une méthode est appelée via un attribut, une VmethodClosure est créée automatiquement :
- Elle lie une fonction définie dans la classe à une instance spécifique de VObject
- Lors de l'appel, 'self' est inséré automatiquement comme premier argument dans un nouvel environnement
- Les autres arguments sont indérés dans l'environnement comme dans un appel classique
- Le corps de la méthode est ensuite exécuté dans ce contexte, et la valeur retournée est soit la valeur de return ou Vnone
Cette structure permet de reproduire le comportement des méthodes orientée objet en Python

