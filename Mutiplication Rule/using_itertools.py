from itertools import islice
from itertools import product

def compound_exp(a,b):
    A = (f"A{i}" for i in range(1, a+1))
    B = (f"B{j}" for j in range(1, b+1))
    return list(product(A, B))

result = compound_exp(3, 2)
length = len(result)
for i in range(length):
    print(result[i])
    
