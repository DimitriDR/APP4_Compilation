import sys

current = {}
previous = {}
position = 0


def next_in_string():
    global position

    text = "1234567 int main() {'" \
           "    a = 3;" \
           "    return 0" \
           "}"

    text_length = len(text)

    # Boucle parcourant toute la chaîne récupérée depuis le fichier
    while position < text_length:

        if text[position].isnumeric():
            buffer = text[position]
            position = position + 1

            while text[position] != text_length and text[position].isnumeric():
                buffer = buffer + "" + text[position]
                print(buffer)

        # print(text[i])

    # return 1


# Token à implémenter prioritairement EOS / CONST / IDENT / ( / ) / { / } / ; / return / int
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Pas d'argument passé en ligne de commande")
        exit(1)

    file = sys.argv[1]
    index = file.rfind('.')

    if index == -1 or (index != len(file) - 2 and file[index + 1] != 'c'):
        print("Erreur d'extension de fichier")
        exit(200)

    file_descriptor = open(file, 'r')
    txt = file_descriptor.read()
    print(txt)

    # next_in_string()
    # while next_in_string() != StopIteration:
    # print("Previous" + previous)
    # print("Current" + current)
