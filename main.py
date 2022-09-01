import sys

current = {}
previous_token = {}
# Défini la position du curseur dans la chaîne de caractères
position = 0
ligne = 0
special_characters = ["/", "(", ")", "{", "}", ";", "="]
keywords = ["int", "return"]


def next_in_string(text: str):
    global position, ligne, previous_token, current

    text_length = len(text)

    # Boucle parcourant le texte passé en paramètre pour évaluer chacun des caractères de celui-ci
    while position < text_length:
        read_char = text[position]
        buffer = None

        # Si on rencontre un espace, on l'ignore, et on incrémente notre position
        if read_char.isspace():
            position = position + 1
            continue

        # Si le caractère à la position p n'est ni un caractère alphanumérique, ni un caractère autorisé,
        # alors le caractère n'est pas valide et une erreur est retournée.
        if not read_char.isalpha() and not read_char.isnumeric() and not (read_char in special_characters):
            exit(200)

        # Si le caractère est bien un caractère alphanumérique,
        # on va continuer de parcourir la chaîne pour en dégager un token
        elif read_char.isalpha():
            # Initialisation du buffer par le premier caractère valide que l'on trouve
            buffer = read_char
            # On augmente la position pour poursuivre sur la chaîne
            position = position + 1

            while position < text_length:
                read_char = text[position]
                if read_char.isalpha() or read_char.isnumeric():
                    buffer = buffer + read_char
                    position = position + 1
                else:
                    break

            # Si current est un dictionnaire vide, inutile de le sauvegarder dans previous
            if current != {}:
                previous_token = current

            current["Type"] = "IDENT"
            current["Valeur"] = buffer

            return

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

            if current != {}:
                previous_token = current

            current["Type"] = "CONST"
            current["Valeur"] = buffer

            return

        elif read_char in special_characters:
            position = position + 1
            return read_char


# Token à implémenter prioritairement EOS / CONST / IDENT / ( / ) / { / } / ; / return / int
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Pas d'argument passé en ligne de commande")
        exit(100)

    file = sys.argv[1]
    index = file.rfind('.')

    if index == -1 or (index != len(file) - 2 and file[index + 1] != 'c'):
        print("Erreur d'extension de fichier")
        exit(101)

    file_descriptor = open(file, "r")
    txt = file_descriptor.read()

    print(next_in_string(txt))
    print(current)
    print(next_in_string(txt))
    print(current)
    print(next_in_string(txt))
    print(next_in_string(txt))
    print(next_in_string(txt))
    print(next_in_string(txt))
    print(next_in_string(txt))
    print(current)
    print(next_in_string(txt))
    print(next_in_string(txt))
    print(current)
    print(next_in_string(txt))
    print(next_in_string(txt))

    print(next_in_string(txt))
