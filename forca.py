from time import sleep
import funcoes

while True:
	
	# Escolha de uma palavra aleatória
	palavra = funcoes.escolhe_palavra()

	# Executa o jogo
	acabou = funcoes.jogo(palavra)
	funcoes.verifica(palavra, acabou)
	novamente = funcoes.de_novo(acabou)
	if novamente == "N":
		break

print("Obrigado por jogar a forca!")
sleep(5)
