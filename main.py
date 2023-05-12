import os
import random
import math
import matplotlib.pyplot as plt
import csv

from generate import gen
from AVLtree import Node, AVL_Tree
from RBtree import Node, RB_Tree
from execute import run
from visualize import print_out

A = 1e6 - 1e3
B = 1e6

def main():
    gen(A, B)
    res = run()
    print_out(res)

if __name__ == "__main__":
    main()