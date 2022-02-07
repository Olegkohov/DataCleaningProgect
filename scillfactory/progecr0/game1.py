"""Игра угадай число"""

import numpy as np

def random_predict(number: int = 1) -> int:
    cislo = np.random.randint(1, 101)
    count = 0
    print(cislo)
    if number > cislo:
        count += 1
        while number > cislo:
            number -= 10
            count += 1
            if number < cislo:
                while True:
                    number += 1
                    count += 1
                    if number == cislo:
                        return count
            if number == cislo:
                return count
    elif number < cislo:
        count += 1
        while number < cislo:
            number += 10
            count += 1
            if number > cislo:
                while True:
                    count += 1
                    number -= 1
                    if number == cislo:
                        return count 
            if number == cislo:
                return count
                         
                    
    else:
        return 1
print(random_predict(1))