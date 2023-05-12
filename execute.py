import os
import math

from AVLtree import Node, AVL_Tree
from RBtree import Node, RB_Tree

def run():
    path = "result.csv"
    with open(path, 'w') as file:
        file.write("avl_tree_height,rb_tree_height,logN,1.45logN\n")
        for i in range(10):
            print(f"[-] Calculating dataset{i}...")
            with open(os.path.join("data", f"data{i}.txt"), 'r') as f:
                numbers = [int(n.strip()) for n in f.readlines()]

                BASE = len(numbers)
                LOGN = math.log2(BASE)
                KLOGN = 1.45 * LOGN

                ## AVL TREE INSERTION
                avl = AVL_Tree()
                root = None
                for num in numbers:
                    root = avl.insert(root, num)
                # print(root.height)
                avl = root.height
                print("     [+] Finish AVL Tree...")

                ## RB TREE INSERTION
                rb = RB_Tree()
                for num in numbers:
                    rb.insert(num)
                # print(rb.getHeight(rb.get_root()) - 1)
                rb = rb.getHeight(rb.get_root()) - 1
                print("     [+] Finish RB Tree...")

                file.write(f"{avl},{rb},{LOGN},{KLOGN}\n")
            print(f"[-] Finish calculating dataset{i}...")
        print("--------------------")
        print("Finish calculating!")
        print(f"Result has been saved at {path}")
    
    return path