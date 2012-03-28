#!/usr/bin/env python

class Node:
    lft = None
    rgt = None
    def __init__(self, key, val):
        self.key = key
        self.val = val   

def insert(node, key, val):
    
    if node is None: return Node(key, val)
    
    if node.key == key: node.val = val
    elif key < node.key:
        
         node.lft = insert(node.lft, key, val)   
    else:
        #A la derecha!
         node.rgt = insert(node.rgt, key, val)   
    return node
            
def search(node, key):
    #Hoja Vacia: Si no esta presente
    if node is None: raise KeyError
    #Buscando Key: retorna valor
    if node.key == key:
        #Menor que key
        return node.val                         
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
    
    
    class Node:
    lft = None
    rgt = None
    def __init__(self, key, val):
        self.key = key
        self.val = val

def insert(node, key, val):
    if node is None: return Node(key, val)      #Hoja Vacia: adiciona un nodo
    if node.key == key: node.val = val          #Key que se encuentra: reemplaza por valor
    elif key < node.key:                        #key es menor
        node.lft = insert(node.lft, key, val)   #A la izquierda
    else:                                       
        node.rgt = insert(node.rgt, key, val)   #A la derecha
    return node

def search(node, key):
    if node is None: raise KeyError             # Hoja Vacia: adiciona un nodo
    if node.key == key: return node.val         # Found key: Return val
    elif key < node.key:                        # key es menor
        return search(node.lft, key)            # A la izquierda
    else:                                      
        return search(node.rgt, key)            # A la derecha

class Tree:                                     # Donde nace el algoritmo
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)
    def __getitem__(self, key):
        return search(self.root, key)
    def __contains__(self, key):
        try: search(self.root, key)
        except KeyError: return False
        return True