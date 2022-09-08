import sys

from node import Node

current = {}
last = {}
# Défini la position du curseur dans la chaîne de caractères
position = 0
# Variable gardant la ligne en mémoire pour savoir à quelle ligne se situe le token
ligne = 1
special_characters = {"/": "tok_slash", "(": "tok_parouvr", ")": "tok_ferm", "{": "tok_accouvr", "}": "tok_accferm",
                      ";": "tok_ptvirg", "=": "tok_affect", "+": "tok_plus", "*": "tok_star", "-": "tok_minus",
                      "!": "tok_exclam", "<": "tok_inf", ">": "tok_sup", ">=": "tok_supEgal", "<=": "tok_infEgal",
                      "!=": "tok_diff",
                      "==": "tok_egal", "&&": "tok_and", "||": "tok_or"}
keywords = ["int", "return", "if", "for", "while", "do", "break", "continue", "else"]
variables = {}

tab_binaire = {
    "tok_star": {"prio": 6, "ag": 1, "noeud": "nd_mult"},
    "tok_slash": {"prio": 6, "ag": 1, "noeud": "nd_div"},
    "tok_mod": {"prio": 6, "ag": 1, "noeud": "nd_mod"},
    "tok_plus": {"prio": 5, "ag": 1, "noeud": "nd_add"},
    "tok_minus": {"prio": 5, "ag": 1, "noeud": "nd_sub"},
    "tok_sup": {"prio": 4, "ag": 1, "noeud": "nd_sup"},
    "tok_inf": {"prio": 4, "ag": 1, "noeud": "nd_inf"},
    "tok_supEgal": {"prio": 4, "ag": 1, "noeud": "nd_supEgal"},
    "tok_infEgal": {"prio": 4, "ag": 1, "noeud": "nd_infEgal"},
    "tok_egal": {"prio": 4, "ag": 1, "noeud": "nd_egal"},
    "tok_diff": {"prio": 4, "ag": 1, "noeud": "nd_diff"},
    "tok_and": {"prio": 3, "ag": 1, "noeud": "nd_and"},
    "tok_or": {"prio": 2, "ag": 1, "noeud": "nd_or"},
    "tok_affect": {"prio": 1, "ag": 0, "noeud": "nd_affect"},
}

# Partie analyseur lexical

"""
Fonction permettant pour un texte donné, de le parcourir et d'en extraire les tokens
"""


def extract_tokens(text: str):
    global ligne, position, special_characters, keywords, variables
    text_length = len(text)
    tab_token = []

    # Boucle parcourant le texte passé en paramètre pour évaluer chacun des caractères de celui-ci
    while position < text_length:
        read_char = text[position]

        # Si on trouve un retour à la ligne, on incrémente la variable correspond et on continue de déplacer le curseur
        if read_char == "\n":
            ligne = ligne + 1
            position = position + 1
            continue

        # Si on rencontre un espace, on l'ignore, et on incrémente notre position
        if read_char.isspace():
            position = position + 1
            continue

        # Si le caractère à la position p n'est ni un caractère alphanumérique, ni un caractère autorisé,
        # alors le caractère n'est pas valide et une erreur est retournée.
        if not read_char.isalpha() and not read_char.isnumeric() and not (read_char in special_characters):
            exit("Caractère non reconnu à la ligne " + str(ligne))

        # Si le caractère est bien un caractère alphanumérique,
        # on va continuer de parcourir la chaîne pour en dégager un token
        elif read_char.isalpha():
            # Initialisation du buffer par le premier caractère valide que l'on trouve
            buffer = read_char
            # On augmente la position pour poursuivre sur la chaîne
            position = position + 1

            # On continue d'évoluer dans le texte pour récupérer le prochain caractère
            # Le prochain caractère peut être une lettre ou un chiffre.
            while position < text_length:
                read_char = text[position]

                if read_char.isalpha() or read_char.isnumeric():
                    buffer = buffer + read_char
                    position = position + 1
                else:
                    break

            if buffer in keywords:
                tab_token.append({"type": "tok_" + buffer, "valeur": buffer, "ligne": ligne})
            else:
                id_var = variables.get(buffer)
                if id_var is None:
                    id_var = len(variables)
                    variables[buffer] = len(variables)
                tab_token.append({"type": "IDENT", "valeur": id_var, "ligne": ligne})

            continue

        elif read_char.isnumeric():
            buffer = read_char
            # On augmente la position pour poursuivre sur la chaîne
            position = position + 1

            while position < text_length:
                read_char = text[position]
                if read_char.isnumeric():
                    buffer = buffer + read_char
                    position = position + 1
                else:
                    break

            tab_token.append({"type": "const", "valeur": buffer, "ligne": ligne})
            continue

        elif read_char in special_characters:
            # TODO: Ajouter support pour && et ||
            #

            # On ajoute le caractère actuel dans un buffer qui servira ... ou pas
            special_characters_buffer = read_char

            # Si la position incrémentée est différente du nombre
            # total de caractère, alors on va pouvoir regarder le buffer
            if position + 1 != text_length:
                pos_temp = position + 1
                special_characters_buffer += text[pos_temp]

                if special_characters_buffer in special_characters:
                    tab_token.append({"type": special_characters[special_characters_buffer], "valeur": special_characters_buffer, "ligne": ligne})
                    position += 2
                else:
                    tab_token.append({"type": special_characters[read_char], "valeur": read_char, "ligne": ligne})
                    position += 1
            else:
                # Si la position suivante atteint la fin de la chaîne alors,
                # on enregistre le dernier caractère, incrémente la position et laisse dérouler l'algorithme.
                tab_token.append({"type": special_characters[read_char], "valeur": read_char, "ligne": ligne})
                position += 1

    tab_token.append({"type": "EOS", "valeur": "EOS", "ligne": ligne})
    position = 0

    return tab_token


"""
Fonction permettant d'obtenir le token suivant
"""


def next():
    global position, list_tok, current, last
    last = current
    current = list_tok[position]
    position = position + 1


def check(token_type) -> bool:
    if current["type"] is token_type:
        next()
        return True
    else:
        return False


def accept(token_type):
    if not check(token_type):
        raise Exception("Le type ne correspond pas")


# Partie analyseur syntaxique
def SA() -> Node:
    if current["Type"] != "EOS":
        raise Exception
    return None


def G() -> Node:
    return F()


def F() -> Node:
    return I()


def I() -> Node:
    return E()


def E() -> Node:
    return Ex(0)


def Ex(prioMin) -> Node:
    a1 = P()
    while (current.type in tab_binaire):
        op = current.type
        if (tab_binaire[op].prio >= prioMin):
            next()
            A2 = Ex(tab_binaire[op].prio + tab_binaire[op].ag)
            A1 = Node(tab_binaire[op].noeud, "", "", [A1, A2])
        else:
            break
    return A1


def P() -> Node:
    if check("tok_minus"):
        N = P()
        M = Node("nd_minus", "-", last["ligne"], [])
        M.add_child(N)
        return M
    elif check("token_plus"):
        P()
    elif check("tok_exclam"):
        return Node("nd_neg", '!', last["ligne"], [P()])
    else:
        return S()


def S() -> Node:
    return A()


def A() -> Node:
    if (check("tok_const")):
        return Node("tok_const", last.valeur, last["ligne"])
    else:
        if (check("tok_parouvr")):
            N = E()
            accept("tok_parferm")

    exit("Erreur de syntaxe à la ligne " + current["ligne"])


# Analyseur sémantique
def ASe():
    N = As()
    return N


# Générateur de pseudo-code
def genCode():
    N = ASe()
    print(".start \n")
    genNode(N)
    print("dbg \n")
    print("hatl")


def genNode(node):
    # A compléter
    # Remplacer le switch case avec des if
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("Pas d'argument passé en ligne de commande")

    file = sys.argv[1]
    index = file.rfind('.')

    if index == -1 or (index != len(file) - 2 and file[index + 1] != 'c'):
        exit("Erreur d'extension de fichier")

    file_descriptor = open(file, "r")
    txt = file_descriptor.readlines()
    txt = "".join(txt)

    list_tok = extract_tokens(txt)
    print(list_tok)
