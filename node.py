# Fichier node.py
# Représente un nœud

class Node:
    node_type = None
    value = None
    line_number = None
    children = None

    """
    Constructeur par défaut initialisant le nœud
    """

    def __init__(self, node_type, value, line_number, children):
        self.node_type = node_type
        self.value = value
        self.line_number = line_number
        self.children = children
