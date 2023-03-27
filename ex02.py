import random

print("Escolha: \nPedra \nPapel \nTesoura")

jg = input()
jg = jg.lower()
sorteio = random.choice(['pedra', 'papel', 'tesoura'])

print(f"O jogador jogou {jg} e o bot jogou {sorteio}")

#Verificação empate
if jg == "pedra" and sorteio == "pedra" or jg == "papel" and sorteio == "papel" or jg == "tesoura" and sorteio == "tesoura":
    print("Empatou")
#Verificação pedra
elif jg == "pedra" and sorteio == "tesoura":
    print("Jogador venceu!")
elif jg == "pedra" and sorteio == "papel":
    print("Bot venceu!")
#Verificação papel
elif jg == "papel" and sorteio == "pedra":
    print("Jogador venceu!")
elif jg == "papel" and sorteio == "tesoura":
    print("Bot venceu!")
#Verificação Tesoura
elif jg == "tesoura" and sorteio == "papel":
    print("Jogador venceu!")
elif jg == "tesoura" and sorteio == "pedra":
    print("Bot venceu!")
