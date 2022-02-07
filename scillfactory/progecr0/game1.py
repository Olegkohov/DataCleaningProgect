"""Игра угадай число"""

import numpy as np

def random_predict(number: int = 1) -> int:
    cislo = np.random.randint(1, 101)
    count = 0 # количество попыток
    print(cislo)
    if number > cislo: #Если наше число больше заданного то мы уменьшаем его на 10 до тех пор пока оно не станет меньше.
        count += 1
        while number > cislo:
            number -= 10
            count += 1
            if number < cislo: #После этого прибавляем 1 пока наше число не станет равно загаданному
                while True:
                    number += 1
                    count += 1
                    if number == cislo:
                        return count
            if number == cislo:
                return count
    elif number < cislo:# Аналогично. Только с нашем числом действия меняются на противоположные 
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
print(random_predict(1)) #Сначала на экране появляется число загаданное компьютором потом количество попыток