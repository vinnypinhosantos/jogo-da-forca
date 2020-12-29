import random

categorias = ["animais", "objetos", "paises", "times"]
categoria = random.choice(categorias)

with open(f'{categoria}.txt', 'r') as f:
	palavras = f.readlines()

palavra = random.choice(palavras)[:-1]

erros_permitidos = 6
acabou = False
chutes = []

print(f"Categoria: {categoria.capitalize()}")

while not acabou:

	for letra in palavra:
		if letra == "-":
			print("-", end='')
			chutes.append(letra)
		elif letra == " ":
			print(" ", end='')
			chutes.append(letra)
		else:
			if letra.lower() in chutes:
				print(f"{letra}", end=' ')
			else:
				print("_", end=' ')
	print()
	chute = input(f"Você ainda pode errar {erros_permitidos} vezes. Seu palpite: ")
	chutes.append(chute)
	
	if chute.lower() not in palavra.lower():
		erros_permitidos -= 1
		if erros_permitidos == 0:
			break

	acabou = True
	for letra in palavra:
		if letra.lower() not in chutes:
			acabou = False

if acabou:
	print(f"Você acertou! A palavra era {palavra}")
else:
	print(f"Game Over! A palavra era {palavra}")
