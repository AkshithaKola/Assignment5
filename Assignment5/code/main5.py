from itertools import product

sets=[['car','apple','bird'],['h','t']]

for S in product(*sets):
    
    print(S)