import random, pygame

pygame.init()

sonC = pygame.mixer.Sound("bruitage/8192.wav")

def getkey(board):
	return ''.join([str(e) for e in sorted(board[0])] + [str(int(board[1]))])
deja_calcule = {}


def getCoupsPossibles(board):  #Coups possibles par l'IA
	allumettes, IA = board
	coups = []
	for i, v in enumerate(allumettes):
		for j in range(v):
			if j < 3:
				newboard = allumettes.copy(), not IA
				newboard[0][i] = v - (j + 1)
				coups.append(newboard)
	return coups


def evaluate(board):	  #Evaluer le meilleur coup possible par l'IA
	allumettes, IA = board

	if getkey(board) in deja_calcule:
		return deja_calcule[getkey(board)]

	if sum(allumettes) is 0:
		if IA:
			return 1
		else:
			return -1

	evals = [evaluate(b) for b in getCoupsPossibles(board)]
	if IA:
		r = max(evals)
	else:
		r = min(evals)

	deja_calcule[getkey(board)] = r

	return r


def play(board):
	results = [(b, evaluate(b)) for b in getCoupsPossibles(board)]
	sonC.play()
	return random.choice([r[0] for r in results if r[1] is max(list(zip(*results))[1])])



if __name__ == '__main__':
	print(play(([1, 3, 5, 7], False)))
	