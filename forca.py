import random
from time import sleep
import funcoes

while True:
	
	# Escolha de uma palavra aleatória
	palavra = funcoes.escolhe_palavra()

	# Define o número máximo de erros, a lista de chites e uma variavel para terminar o jogo
	erros_permitidos = 6
	acabou = False
	chutes = []

	# Executa o jogo
	acabou = funcoes.jogo(palavra, acabou, chutes, erros_permitidos)
	funcoes.verifica(palavra, acabou)
	novamente = funcoes.de_novo(acabou)
	if novamente == "N":
		break

print("Obrigado por jogar a forca!")
sleep(5)
