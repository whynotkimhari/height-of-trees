import random
import os

def gen(a, b):
    for i in range(10):
        path = f"data{i}.txt"
        with open(os.path.join("data", path), 'w', encoding='utf8') as file:
            ### a -> b: randomly
            rd = random.randint(a, b)
            print(f"[!] Generating data{i}.txt with size: {rd}")
            for _ in range(rd):
                file.write(f"{random.randint(0, 1000000000)}\n")