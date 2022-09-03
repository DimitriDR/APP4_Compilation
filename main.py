import sys

current = {}
last = {}
# Défini la position du curseur dans la chaîne de caractères
position = 0
# Variable gardant la ligne en mémoire pour savoir à quelle ligne se situe le token
ligne = 1
special_characters = {"/": "tok_slash", "(": "tok_parouvr", ")": "tok_ferm", "{": "tok_accouvr", "}": "tok_accferm",
                      ";": "tok_ptvirg", "=": "tok_affect", "+": "tok_plus", "*": "tok_star"}
keywords = ["int", "return", "if", "for", "while", "do", "break", "continue", "else"]
variables = {}

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

        elif read_char in special_characters:  # reste  à traiter le cas des caractere speciaux comportant 2 carcatères
            # reste à traiter le cas des dièses
            position = position + 1
            tab_token.append({"type": special_characters[read_char], "valeur": read_char, "ligne": ligne})
            continue

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
