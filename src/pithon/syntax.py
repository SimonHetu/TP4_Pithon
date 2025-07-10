from dataclasses import dataclass

@dataclass
class PiNone:
    value: None

@dataclass
class PiNumber:
    value: float

@dataclass
class PiBool:
    value: bool

@dataclass
class PiVariable:
    name: str

@dataclass
class PiBinaryOperation:
    left: 'PiExpression'
    operator: str
    right: 'PiExpression'

@dataclass
class PiAssignment:
    name: str
    value: 'PiExpression'

@dataclass
class PiIfThenElse:
    condition: 'PiExpression'
    then_branch: list['PiStatement']
    else_branch: list['PiStatement']

@dataclass
class PiNot:
    operand: 'PiExpression'

@dataclass
class PiAnd:
    left: 'PiExpression'
    right: 'PiExpression'

@dataclass
class PiOr:
    left: 'PiExpression'
    right: 'PiExpression'

@dataclass
class PiWhile:
    condition: 'PiExpression'
    body: list['PiStatement']

@dataclass
class PiList:
    elements: list['PiExpression']

@dataclass
class PiTuple:
    elements: tuple['PiExpression', ...]

@dataclass
class PiString:
    value: str

@dataclass
class PiFunctionDef:
    name: str
    arg_names: list[str]
    vararg: str | None
    body: list['PiStatement']

@dataclass
class PiFunctionCall:
    function: 'PiExpression'
    args: list['PiExpression']

@dataclass
class PiFor:
    var: str
    iterable: 'PiExpression'
    body: list['PiStatement']

@dataclass
class PiBreak:
    pass

@dataclass
class PiContinue:
    pass

@dataclass
class PiIn:
    element: 'PiExpression'
    container: 'PiExpression'

@dataclass
class PiReturn:
    value: 'PiExpression'

@dataclass
class PiSubscript:
    collection: 'PiExpression'
    index: 'PiExpression'

@dataclass
class PiClassDef: # Syntaxe pour la définition de classe
    name: str # Le nom de la classe sous forme de chaine de caractère
    methods: list['PiFunctionDef'] 
    # Liste des  définitions de méthodes contenues dans la classe
    # Chaque élément est une instance de PiFunctionDef, qui contiendra son propre nom, ses parametres et son corps

@dataclass
class PiAttribute: # Représente l'accès à la lecture de l'attribut d'un objet
    object: 'PiExpression' # Expression représentant l'objet
    attr: str # Nom de l'attribut auquel on veut accéder

@dataclass
class PiAttributeAssignment: # Représente l'assignation d'une valeur à un attribut d'un objet 
    object: 'PiExpression' # Expression représentant l'objet ciblé
    attr: str # Nom de l'attribut à modifier ou à créer
    value: 'PiExpression'# Valeur à attribuer à cet attribut

PiValue = PiNumber | PiBool | PiNone | PiList | PiTuple | PiString

PiExpression = (
    PiValue
    | PiVariable
    | PiBinaryOperation
    | PiNot
    | PiAnd
    | PiOr
    | PiFunctionCall
    | PiIn
    | PiSubscript
    | PiAttribute
    | PiAttributeAssignment
)

PiStatement = (
    PiAssignment
    | PiAttributeAssignment
    | PiIfThenElse
    | PiWhile
    | PiFor
    | PiBreak
    | PiContinue
    | PiFunctionDef
    | PiClassDef
    | PiReturn
    | PiExpression
)

PiProgram = list[PiStatement]
