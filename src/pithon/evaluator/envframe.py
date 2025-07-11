class EnvFrame:
    """
    Représente un cadre d'environnement pour stocker des variables avec un lien vers un parent.
    """
    def __init__(self, parent=None):
        """
        Initialise un nouvel environnement, éventuellement avec un parent.
        """
        self.vars = {} # Dictionnaire vide qui contiendra les variable locales de cet environnement
        self.parent: EnvFrame | None = parent # Référence à un environnement parent, pour gérer les portées imbriquées

    def lookup(self, name):
        """
        Recherche la valeur d'une variable par son nom dans l'environnement courant ou ses parents.
        """
        if name in self.vars: # Vérifie si la variable est définie localement 
            return self.vars[name]
        elif self.parent is not None: # Sinon recherche récursivement dans le parent (portées extérieures)
            return self.parent.lookup(name)
        else:
            raise NameError(f"Variable '{name}' non définie.") # Si aucune des portées ne contient la variable une erreur est levée

    def insert(self, name, value): # Ajoute une nouvelle variable ou écrase sa valeur si elle existe déjà
        """
        Insère ou met à jour une variable dans l'environnement courant.
        """
        self.vars[name] = value

    def copy_shallow(self):
        """
        Retourne une copie superficielle de l'environnement (variables copiées, même parent).
        """
        newf = EnvFrame(self.parent) # Crée un nouveau frame avec le même parent et la même portée extérieure
        newf.vars = self.vars.copy() # Création d'un nouveau dictionnaire avec les mêmes paires clé-valeur
        return newf