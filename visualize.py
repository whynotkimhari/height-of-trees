import matplotlib.pyplot as plt
import csv

def print_out(path):
    y = [i for i in range(10)]

    with open(path, 'r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        avl = []
        rb = []
        logN = []
        klogN = []
        
        for row in reader:
            avl.append(float(row['avl_tree_height']))
            rb.append(float(row['rb_tree_height']))
            logN.append(round(float(row['logN']), 2))
            klogN.append(round(float(row['1.45logN']), 2))

        plt.plot(y, avl, label="avl")
        plt.plot(y, rb, label="rb")
        plt.plot(y, logN, label="logn")
        plt.plot(y, klogN, label="1.45logn")
        plt.legend()
        plt.savefig('chart.png')
        plt.show()
        plt.close()