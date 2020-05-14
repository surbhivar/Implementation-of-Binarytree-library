# Creating binary tree
# from given list
from binarytree import build
import random

def random_component():
    n = random.randint(0,3)  # equal chance for each component type
    if n == 0:
        component = 1    #generates 1
    if n == 1:
        component = 2    #generates 2
    if n ==2 :
        component = 3    #generates 3

    return component

comp1=random_component()
comp2=random_component()
comp3=random_component()
comp4=random_component()
comp5=random_component()
comp6=random_component()

# List of nodes
nodes =[comp1,comp2 ,comp3, comp4, comp5, comp6]

# Builidng the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
      binary_tree)

# Getting list of nodes from
# binarytree
print('\nList from binary tree :',
      binary_tree.values)
