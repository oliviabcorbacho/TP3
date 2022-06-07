import colorama


def username():
    username = input("Enter your username: ")
    return username

def fibonacci_sequence(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
def recursive_fibonacci_sequence(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci_sequence(n - 1) + recursive_fibonacci_sequence(n - 2)

#%%
from colorama import Fore, Back, Style
print(Fore.RED + "Some red text")


# %%
import numpy as np
import matplotlib.pyplot as plt

class Alumno:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
        self.notas = 0
    
    def nota_de_cursada(self):
        if len(self.notas) == 0:
            return 0
        return np.mean(self.notas)

    def obtener_nota(self):
        return np.array(self.notas)
    
    def cargar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        
    def __lt__(self, other):
        return self.nota_de_cursada() < other.nota_de_cursada()

    def __eq__(self, other):
        return self.nota_de_cursada() == other.nota_de_cursada()
    
    def __repr__(self) -> str:
        return f"Alumno('{self.nombre}')"

# %%
