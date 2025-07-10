"""Définitions des valeurs pour l'évaluateur Pithon."""

from typing import Union,  Callable
from dataclasses import dataclass
from pithon.syntax import ( PiFunctionDef,
)
from pithon.evaluator.envframe import EnvFrame

PrimitiveFunction = Callable[..., 'EnvValue']

@dataclass
class VFunctionClosure:
    """Représente une fermeture de fonction avec son environnement."""
    funcdef: PiFunctionDef
    closure_env: EnvFrame

    def __str__(self) -> str:
        return f"<function {self.funcdef.name} at {id(self)}>"

@dataclass
class VList:
    """Représente une liste de valeurs."""
    value: list['EnvValue']

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)

@dataclass
class VTuple:
    """Représente un tuple de valeurs."""
    value: tuple['EnvValue', ...]

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)

@dataclass
class VNumber:
    """Représente un nombre (float)."""
    value: float

    def __str__(self) -> str:
        return str(self.value)


    def __repr__(self) -> str:
        return repr(self.value)

@dataclass
class VBool:
    """Représente une valeur booléenne."""
    value: bool

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)

@dataclass
class VNone:
    """Représente la valeur None."""
    value: None = None

    def __str__(self) -> str:
        return str(None)

    def __repr__(self) -> str:
        return repr(self.value)

@dataclass
class VString:
    """Représente une chaîne de caractères."""
    value: str

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)

@dataclass
class VClassDef: # Valeur d'une définition de classe, utilisée lors de l'exécution d'un noeud PiClassDef
    """Représente une définition de classe avec ses méthodes."""
    name: str
    methods: dict[str, VFunctionClosure]
    # Dictionnaire associant le nom de chaque méthode à une VFunctionClosure
    # Chaque VFunctionClosure encapsule la fonction et l'environnement où elle a été définie,
    # Ce qui permet à la méthode de conserver l'accès à sa portée d'origine même lorsqu'elle est utilisée ailleur
    def __str__(self) -> str:
        return f"<class {self.name} at {id(self)}>"

@dataclass
class VObject:
    """Représente une instance d'une classe avec ses attributs."""
    class_def: VClassDef 
    # Lie l'objet à la definition de classe, qui contient les méthodes et leurs environnements de création

    attributes: dict[str, 'EnvValue'] 
    # Dictionnaire des attributs propres à cette instance
    # Contient des paires nom valeur pour chaque attribut défini ou assigné sur l'objet
    # Ce dictionnaire distinct des méthodes de la classe qui sont stockées dans class_def.methods

    def __str__(self) -> str: 
    # Méthode spéciale utilisée lors de l'affichage de l'objet 
    # Renvoie une chaine lisible avec le nom de la classe et un identifiant unique
        return f"<{self.class_def.name} object at {id(self)}>"

    def __repr__(self) -> str:
    # Méthode spéciale utilisée dans les contextes interactifs ou les listes d'objets
    # Ici, elle renvoie simplement le résultat de __str__
        return self.__str__()

@dataclass
class VMethodClosure: # Permet de lier une fonction de class à une instance contrète comme self
    """Représente une méthode liée à une instance."""
    function: VFunctionClosure
    # Fonction définie dans la classe avec son environnement lexical (portée de définition)
    instance: VObject # L'instance à laquelle la méthode est liée, joue le role de 'self' lors de l'appel
    # Ce qui rend possible le comportement attendu en Python : 
    # - accès aux attributs de l'objet et partage de l'état
    # - conservation et partage de l'état interne

    def __str__(self) -> str: # Méthode spéciale pour l'affichage en chaine lisible
        return f"<method {self.function.funcdef.name} of {self.instance.class_def.name} at {id(self)}>"

    def __repr__(self) -> str: # Représentation pour les contextes intéractifs ici identique à __str__
        return self.__str__()

EnvValue = Union[
    VNumber,
    VBool,
    VNone,
    VString,
    VList,
    VTuple,
    VObject,
    VFunctionClosure,
    VMethodClosure,
    VClassDef,
    PrimitiveFunction
]
