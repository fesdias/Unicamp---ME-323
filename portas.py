#Porta dos desesperados
#Felipe Santana Dias - RA: 215775
#Letícia Adrielle Luz - RA: 220208

import matplotlib.pyplot as plt
from random import randint

def p(vit, total):
    return (vit / total)


#Caso 1 - Troca as portas
x = []
y = []

vitoria = 0
for i in range(1, 10001):

    premio = randint(1, 3)
    escolha = randint(1, 3)

    if premio == escolha:
        vitoria += 1
        continue

    else:
        nova_escolha = randint(1, 3)
        while nova_escolha == escolha:
            nova_escolha = randint(1, 3)

        if premio == nova_escolha:
            vitoria += 1

    x.append(i)
    y.append(p(vitoria, i))

plt.title('Porta dos desesperados')
plt.suptitle('Caso 1 - Troca de portas')
plt.xlabel('Tentativas')
plt.ylabel('Proporção acumulada')
plt.plot(x, y)
plt.show()

#Caso 2 - mantém a porta
x1 = []
y1 = []

vitoria = 0
for i in range(1, 10001):

    premio = randint(1, 3)
    escolha = randint(1, 3)

    if premio == escolha:
        vitoria += 1

    x1.append(i)
    y1.append(p(vitoria, i))

plt.title('Porta dos desesperados')
plt.suptitle('Caso 2 - Mantém a porta')
plt.xlabel('Tentativas')
plt.ylabel('Proporção acumulada')
plt.plot(x1, y1)
plt.show()