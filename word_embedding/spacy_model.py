from enum import Enum, auto
import nltk
import spacy
from nltk.tokenize import word_tokenize

from tokencontainer import GrammarCategories

class SpacyModel:
    def load(self, sentence:str):
        self.words = sentence
        self.spacytokens = self.model(sentence)

    def __init__(self):
        self.model = spacy.load("en_core_web_sm")
        self.spacytokens = None

    words = ""
    keyvector = ""

    def tokens(self):
        #list_of_strings = self.words.split(" ")
        list_of_tokens = []
        for spacytoken in self.spacytokens:
            name = spacytoken.text
            pos_tag = self.get_pos_tag_from_spacytoken(spacytoken)
            dependency = self.get_dependency_from_spacytoken(spacytoken)

            new_token = Token(name, pos_tag, dependency)
            list_of_tokens.append(new_token)
        return list_of_tokens

    def get_dependency_from_spacytoken(self, spacytoken):
        converter = {
            "nsubj": Dependency.nsubj,
            "pobj": Dependency.pobj
            }
        spacy_dependency = spacytoken.dep_
        print(spacy_dependency)
        if spacy_dependency not in converter.keys():
            return Dependency.other
        else:
            return converter[spacy_dependency]

    def get_pos_tag_from_spacytoken(self, spacytoken):
        space_pos_tag = spacytoken.tag_
        converter = {
            "NN": GrammarCategories.noun,
            "JJ": GrammarCategories.adj,
            "NNP": GrammarCategories.noun}
        if space_pos_tag not in converter.keys():
            return GrammarCategories.other
        else:
            return converter[space_pos_tag]


class Dependency(Enum):
    root = auto()
    nsubj = auto()
    acl = auto()
    acomp = auto()
    advcl = auto()
    advmod = auto()
    agent = auto()
    amod = auto()
    appos = auto()
    attr = auto()
    aux = auto()
    auxpass = auto()
    case = auto()
    cc = auto()
    ccomp = auto()
    compound = auto()
    conj = auto()
    cop = auto()
    csubj = auto()
    csubjpass = auto()
    dative = auto()
    dep = auto()
    det = auto()
    dobj = auto()
    expl = auto()
    intj = auto()
    mark = auto()
    meta = auto()
    neg = auto()
    nn = auto()
    nounmod = auto()
    npmod = auto()
    nsubjpass = auto()
    nummod = auto()
    oprd = auto()
    obj = auto()
    obl = auto()
    parataxis = auto()
    pcomp = auto()
    pobj = auto()
    poss = auto()
    preconj = auto()
    prep = auto()
    prt = auto()
    punct = auto()
    quantmod = auto()
    relcl = auto()
    xcomp = auto()
    other = auto()

class Token:
    pos_tag: GrammarCategories
    dep: Dependency
    name = ""

    def __init__(self, name,pos_tag=None, dep=None):
        self.name = name
        self.pos_tag = pos_tag
        self.dep = dep

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"Token: name:{self.name}"

