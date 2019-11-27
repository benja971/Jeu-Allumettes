import pygame, os, random, time, IA

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

white = (255,255,255)

#Variables
Joueur1 = True
Joueur2 = False
tour = 0
select = 1
end = False
frame = 0
state = "menu"
board = ([1, 3, 5, 7], False)
coups = []


#Sons
sonC = pygame.mixer.Sound("bruitage/sonC.wav")
sonjeux = pygame.mixer.Sound("bruitage/Yes- Roundabout (To Be Continued Song) FREE DOWNLOAD (Audio).wav")
bruitMenu = pygame.mixer.Sound("bruitage/1978.wav")
musicMenu = pygame.mixer.Sound("bruitage/LAKEY INSPIRED - Chill Day.wav")


#Fonctions
def afficherBoard(board):
	for i in range(len(board[0])):
		for j in range(board[0][i]):
			fenetre.blit(bank['whisky'], (j * 95 + 180, i * 140 + 50))


def loadImg():
	return{img.split('.')[0]: pygame.image.load('images/' + img).convert_alpha() for img in os.listdir('images/')}



size = width, height = 971, 673
fenetre = pygame.display.set_mode((size))
rectFenetre = fenetre.get_rect()
pygame.display.set_caption('Le jeu des cacahuete')
horloge = pygame.time.Clock()

bank = loadImg()

#Positions des images et textes
police1 = pygame.font.Font('text/budmo jiggler.ttf', 80) #lose
police2 = pygame.font.Font('text/budmo jiggler.ttf', 26) #joueurs
font = pygame.font.Font('text/budmo jiggler.ttf', 60) #titre menu
font2 = pygame.font.Font('text/budmo jiggler.ttf', 55) #texte du menu

rectBordure = bank['bordureBis'].get_rect()
rectBordure.center = rectFenetre.center
rectBordure.x = 220
rectBordure.y = 200

rectBordure2 = bank['bordureBis'].get_rect()
rectBordure2.center = rectFenetre.center
rectBordure2.x = 213
rectBordure2.y = 325

rectBordure3 = bank['bordureBis2'].get_rect()
rectBordure3.center = rectFenetre.center
rectBordure3.x = 280
rectBordure3.y = 475

rectBordure4 = bank['bordureBis2'].get_rect()
rectBordure4.center = rectFenetre.center
rectBordure4.x = 280
rectBordure4.y = 620

textelosej1 = police1.render('Player1 Lose', True, white)
textelosej2 = police1.render('Player Lose', True, white)

textelosej = police1.render('Player Lose', True, white)
texteloseia = police1.render('IA Lose', True, white)

textjoueur1 = police2.render("Player 1", True, white)
textjoueur2 = police2.render("Player 2", True, white)

imageText = font.render("Menu", 1, (255, 10, 10))
rectText = imageText.get_rect()
rectText.center = rectFenetre.center
rectText.y = 50

imageText2 = font2.render("SinglePlayer", 1, (255, 255, 255))
rectText2 = imageText2.get_rect()
rectText2.center = rectFenetre.center
rectText2.y = 150

imageText3 = font2.render("MultiPlayer", 1, (255, 255, 255))
rectText3 = imageText3.get_rect()
rectText3.center = rectFenetre.center
rectText3.y = 280

imageText4 = font2.render("Infos", 1, (255, 255, 255))
rectText4 = imageText4.get_rect()
rectText4.center = rectFenetre.center
rectText4.y = 420

imageText5 = font2.render("Quit", 1, (255, 255, 255))
rectText5 = imageText5.get_rect()
rectText5.center = rectFenetre.center
rectText5.y = 570

rectPointeur = bank["pointeur"].get_rect()
rectPointeur.x = 50
rectPointeur.y = 60

rectPointeur2 = bank["pointeur0"].get_rect()
rectPointeur2.x = 640
rectPointeur2.y = 160

select = 1

musicMenu.play()

while not end:
	frame += 1
	touches = pygame.key.get_pressed()
	events = pygame.event.get()

	if touches [pygame.K_ESCAPE]:
		end = True

	if touches [pygame.K_TAB]:
		state = "menu"

	for event in events:
		if event.type == pygame.QUIT:
			end = True

	fenetre.blit(bank["fond3"],(0,0))

	if state == "menu":
		horloge.tick(10)

		frame = 0
		ia_frame = 0

		fenetre.blit(imageText, rectText) 
		fenetre.blit(imageText2, rectText2) 
		fenetre.blit(imageText3, rectText3) 
		fenetre.blit(imageText4, rectText4) 
		fenetre.blit(imageText5, rectText5) 

		if touches[pygame.K_DOWN]:
			select += 1
			bruitMenu.play()

		if touches[pygame.K_UP]:
			select -= 1
			bruitMenu.play()

		if select == 1 :
			rectPointeur2.x = 680
			rectPointeur2.y = 160
			fenetre.blit(bank['pointeur0'], rectPointeur2)
			fenetre.blit(bank["bordureBis"], rectBordure.center)
			
			if touches[pygame.K_RETURN]:
				musicMenu.stop()
				state = "SinglePlayer"
				sonjeux.play()
				select = 1

		if select == 2 :
			rectPointeur2.x = 680
			rectPointeur2.y = 285
			fenetre.blit(bank['pointeur0'], rectPointeur2)
			fenetre.blit(bank["bordureBis"], rectBordure2.center)

			if touches [pygame.K_RETURN]:
				state = "MultiPlayer"
				sonjeux.play()
				select = 1

		if select == 3 :
			rectPointeur2.x = 680
			rectPointeur2.y = 425
			fenetre.blit(bank['pointeur0'], rectPointeur2)
			fenetre.blit(bank["bordureBis2"], rectBordure3.center)

			if touches[pygame.K_RETURN]:
				mon_fichier = open("./infos.txt","r")
				contenue = mon_fichier.read()
				print(contenue)
				mon_fichier.close()	

		if select == 4 :
			rectPointeur2.x = 680
			rectPointeur2.y = 575
			fenetre.blit(bank['pointeur0'], rectPointeur2)
			fenetre.blit(bank["bordureBis2"], rectBordure4.center)

			if touches [pygame.K_RETURN]:
				end = True

		if select >= 5 :
			select = 1

		if select == 0 :
			select = 4

		allumettes = [1, 3, 5, 7]



	if state == "SinglePlayer":
		afficherBoard(board)
		musicMenu.stop()
		horloge.tick(15)
		allumettes, ia = board
		
		if sum(allumettes) == 0:
			if ia:
				fenetre.blit(textelosej, (300, 300))
				#state = "menu"
			else:
				fenetre.blit(texteloseia, (300, 300))
				#state = "menu"


		if ia:
			if ia_frame is 0:
				ia_frame = frame
			elif frame - ia_frame >= 10:
				ia_frame = 0
				board = IA.play(board)

		else:
			if touches [pygame.K_DOWN]:
				select += 1
			if touches [pygame.K_UP]:
				select -= 1

			if select == 1 :
				rectPointeur.x = 40
				rectPointeur.y = 80
				fenetre.blit(bank["pointeur4"],rectPointeur)

				if touches [pygame.K_1] and board [0][0] == 1:
					sonC.play()
					board[0][0] -= 1
					ia = True
					board = allumettes, ia
					ia_frame = 0
					
			if select == 2 :
				rectPointeur.x = 40
				rectPointeur.y = 210
				fenetre.blit(bank["pointeur4"],rectPointeur)

				if touches [pygame.K_1] and board[0][1] >= 1:
					sonC.play()
					board[0][1] -= 1
					ia = True
					board = allumettes, ia
					ia_frame = 0

				if touches [pygame.K_2] and board[0][1] >= 2:
					sonC.play()
					board[0][1] -= 2
					ia = True
					board = allumettes, ia
					ia_frame = 0

				if touches [pygame.K_3] and board[0][1] >= 3:
					sonC.play()
					board[0][1] -=3
					ia = True
					board = allumettes, ia
					ia_frame = 0

			if select == 3 :
				rectPointeur.x = 40
				rectPointeur.y = 360
				fenetre.blit(bank["pointeur4"],rectPointeur)

				if touches [pygame.K_1] and board [0][2] >= 1:
					sonC.play()
					board[0][2] -= 1
					ia = True
					board = allumettes, ia
					ia_frame = 0

				if touches [pygame.K_2] and board [0][2] >= 2:
					sonC.play()
					board[0][2] -= 2
					ia = True
					board = allumettes, ia
					ia_frame = 0

				if touches [pygame.K_3] and board [0][2] >= 3:
					sonC.play()
					board[0][2] -=3
					ia = True
					board = allumettes, ia
					ia_frame = 0

			if select == 4 :
				rectPointeur.x = 40
				rectPointeur.y = 510
				fenetre.blit(bank["pointeur4"],rectPointeur)

				if touches [pygame.K_1] and board [0][3] >= 1:
					sonC.play()
					board[0][3] -= 1
					ia = True
					board = allumettes, ia
					ia_frame = 0

				if touches [pygame.K_2] and board [0][3] >= 2:
					sonC.play()
					board[0][3] -= 2
					ia = True
					board = allumettes, ia
					ia_frame = 0

				if touches [pygame.K_3] and board [0][3] >= 3:
					sonC.play()
					board[0][3] -= 3
					ia = True
					board = allumettes, ia
					ia_frame = 0

			if select >= 5 :
				select = 1

			if select == 0 :
				select = 4

	if state == "MultiPlayer":

		afficherBoard(board)
		musicMenu.stop()
		horloge.tick(8)

		if touches [pygame.K_DOWN]:
			select += 1
		if touches [pygame.K_UP]:
			select -= 1

		if select == 1 :
			rectPointeur.x = 40
			rectPointeur.y = 80
			fenetre.blit(bank["pointeur4"],rectPointeur)

			if touches [pygame.K_1] and board [0][0] == 1:
				sonC.play()
				board[0][0] -= 1
				tour += 1


		if select == 2 :
			rectPointeur.x = 40
			rectPointeur.y = 210
			fenetre.blit(bank["pointeur4"],rectPointeur)

			if touches [pygame.K_1] and board[0][1] >= 1:
				sonC.play()
				board[0][1] -= 1
				tour += 1		

			if touches [pygame.K_2] and board[0][1] >= 2:
				sonC.play()
				board[0][1] -= 2
				tour += 1

			if touches [pygame.K_3] and board[0][1] >= 3:
				sonC.play()
				board[0][1] -=3
				tour += 1


		if select == 3 :
			rectPointeur.x = 40
			rectPointeur.y = 360
			fenetre.blit(bank["pointeur4"],rectPointeur)

			if touches [pygame.K_1] and board [0][2] >= 1:
				sonC.play()
				board[0][2] -= 1
				tour += 1		

			if touches [pygame.K_2] and board [0][2] >= 2:
				sonC.play()
				board[0][2] -= 2
				tour += 1

			if touches [pygame.K_3] and board [0][2] >= 3:
				sonC.play()
				board[0][2] -=3
				tour += 1

		if select == 4 :
			rectPointeur.x = 40
			rectPointeur.y = 510
			fenetre.blit(bank["pointeur4"],rectPointeur)

			if touches [pygame.K_1] and board [0][3] >= 1:
				sonC.play()
				board[0][3] -= 1
				tour += 1	

			if touches [pygame.K_2] and board [0][3] >= 2:
				sonC.play()
				board[0][3] -= 2
				tour += 1

			if touches [pygame.K_3] and board [0][3] >= 3:
				sonC.play()
				board[0][3] -= 3
				tour += 1

		if select >= 5 :
			select = 1

		if select == 0 :
			select = 4

		if tour%2 == 0 :
			Joueur1 = True
			fenetre.blit(textjoueur1, (10,0))

		else :
			Joueur2 = True
			fenetre.blit(textjoueur2, (10,0))
			

		if sum(board[0]) == 1:
			if tour%2 == 0:
				fenetre.blit(textelosej2, (300, 300))
			else:
				fenetre.blit(textelosej1, (300, 300))

	pygame.display.flip()
pygame.quit()