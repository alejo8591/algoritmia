#!/usr/bin/env python

class Node:
    lft = None
    rgt = None
def __init__(self, key, val):
        self.key = key
        self.val = val
def insert(node, key, val):
    if node is None: return Node(key, val)      #Hoja Vacia: adiciona un nodo
    if node.key == key: node.val = val          #Key que se encuentra: reemplaza por valor
    elif key < node.key:                        #Menor que key
        node.lft = insert(node.lft, key, val)   #A la izquierda
    else:                                       
        node.rgt = insert(node.rgt, key, val)   #A la derecha!
    return node
            
def search(node, key):
    if node is None: raise KeyError             #Hoja Vacia: Si no esta presente
    if node.key == key:                         #Buscando Key: retorna valor
        return node.val                         #Menor que key
    elif key < node.key:
        return search(node.lft, key)
    else:
        return search(node.rgt, key)

class Tree:
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)
        def __getitem__(self, key): return search(self.root, key)
        def __contains__(self, key):
            try: search(self.root, key)
            except KeyError: return False
            return True