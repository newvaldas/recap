# sukurti funcija, kad grazintu lista jame sugeneratuotu su 6 random integeriais, 
# kurie negali buti maziau uz 0 ir daugiu 100. Listas turi buti nuo min max

# sukurti lista su random
#
#

import random


# def list_generator():
#     my_list = []
#     for x in range(0, 6):
#         my_list.append(random.randint(0, 100))
#     return sorted(my_list)
# print(list_generator())    

def list_generator () -> list:
    # return sorted([random.randint(0, 100) for _ in range (0, 6)])
    my_list = (lambda : sorted([random.randint(0, 100) for _ in range(0, 6) ]))


    
print(list_generator())

