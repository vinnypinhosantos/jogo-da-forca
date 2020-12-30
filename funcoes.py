import random


def escolhe_palavra():
	# Escolhe aleatoriamente a palavra de uma das categorias
	categoria = random.choice(["animais", "objetos", "paises", "times"])

	with open(f'{categoria}.txt', 'r') as f:
		palavras = f.readlines()

	palavra = random.choice(palavras)[:-1]

	print(f"Categoria: {categoria.capitalize()}")

	return palavra


def jogo(palavra):
	# Define o número máximo de erros, a lista de chites e uma variavel para terminar o jogo
	erros_permitidos = 6
	acabou = False
	chutes = []

	while not acabou:
		
		criando_forca(palavra, chutes)
		
		# Pede a letra ao usuário e adiciona na lista de chutes
		chute = input(f"Você ainda pode errar {erros_permitidos} vezes. Seu palpite: ")
		chutes.append(chute)
			
		# Verifica se o chute não está na palavra e tira uma chance do usuário até chegar a 0
		if chute.lower() not in palavra.lower():
			erros_permitidos -= 1
			if erros_permitidos == 0:
				break
		
		# Se o usuário acertou o loop acaba, se não o loop recomeça
		acabou = True
		for letra in palavra:
			if letra.lower() not in chutes:
				acabou = False

	return acabou


def verifica(palavra, acabou):
	# Mostra se o usuário acertou ou não
	if acabou:
		print("-" * 20)
		print(f"Você acertou! A palavra era {palavra}")
	else:
		print("-" * 20)
		print(f"Game Over! A palavra era {palavra}")


def de_novo(acabou):
	# Verifica se o usuário quer jogar de novo
	while True:
		print("-" * 20)
		novamente = input("Quer jogar de novo? [S/N]").upper()
		print("-" * 20)
		if novamente == "N":
			acabou = True
			break
		elif novamente == "S":
			acabou = False
			break
		else:
			print("Digite S ou N para escolher!")
	return novamente


def criando_forca(palavra, chutes):
	# Percorre a palvra e escreve os espaços e letras
	for letra in palavra:
		# Escreve os traços e espaços
		if letra == "-":
			print("-", end='')
			chutes.append(letra)
		elif letra == " ":
			print("  ", end='')
			chutes.append(letra)
		else:
			# Verifica se a letra "chutada" está na palavra
			if letra.lower() in chutes:
				print(f"{letra}", end=' ')
			else:
				print("_", end=' ')
	print()

	
