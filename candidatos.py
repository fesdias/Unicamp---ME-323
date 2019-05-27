#Candidatos A e B
#Felipe Santana Dias - RA: 215775
#Letícia Adrielle Luz - RA: 220208

import matplotlib.pyplot as plt
from random import randint
import numpy as np
import math

def perAmostra(n):
    votaA = 0

    for i in range(n):

        pessoa = randint(1, 10000)

        if (pessoa <= 3000):
            votaA += 1

    return votaA/n

def proporcao(amostra):
    x = []
    y = []
    soma = 0

    for i in range(2000):
        x.append(i)

        p = perAmostra(amostra)
        y.append(p)
        soma += p

    media = soma/2000
    variancia = np.var(y)
    desvio = math.sqrt(variancia)

    plt.title('Candidato A ')
    plt.suptitle('n = 100')
    plt.xlabel('Amostra')
    plt.ylabel('"P Chapéu" de A')
    plt.plot(x, y)
    plt.show()
    plt.savefig("temp.png")

    print("Amostra aleatória de tamanho ", amostra, " com reposição ")
    print("Media = ", media)
    print("Desvio Padrão = ", desvio)
    print("\n")

proporcao(1000)
