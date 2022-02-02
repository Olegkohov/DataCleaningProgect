"""Игра угадай число"""

import numpy as np

def random_predict(number: int = 1) -> int:
    number = np.random.randint(1, 101) # загадываем число
