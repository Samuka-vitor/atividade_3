"""
Crie um programa que controle a entrada de usuários no brinquedo "Trem fantasma" de um parque de diversão. 
O programa só deve autorizar a entrada de usuários que possuem mais de 10 anos e menos de 150kg de peso. 
Ao terminar, envie para o GitHub.

"""

print("Olá, por gentileza, me responda algumas perguntas.")

nome= input("Qual seu nome?")
idade= int(input("Qual sua idade?"))
peso= int(input("Por motivos de segurança, gostariamos de saber seu peso. Qual seu peso?"))

if idade <= 10:
    print("Desculpa, mas você não tem idade suficiente para ir no briquendo.")
elif peso >= 150:
    print("Desculpa, mas você está acima do peso, para a sua segurança, não será permitido sua entrada.")
else:
    print("Tudo certo, pode prosseguir. Boa experiência.")

