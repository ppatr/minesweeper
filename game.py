﻿import pygame
import os

class Game():
	def __init__(self, board, screenSize):
		self.board = board
		self.screenSize = screenSize
		self.pieceSize = self.screenSize[0] // self.board.getSize() [1], self.screenSize[1] // self.board.getSize()[0]
		self.loadImages()

	def run(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.screenSize)
		running = True
		while running:
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					running = False
				if (event.type == pygame.MOUSEBUTTONDOWN):
					position = pygame.mouse.get_pos()
					self.handleClick(position)
			self.draw()
			pygame.display.flip()
		pygame.QUIT()

	def draw(self):
		topLeft = (0, 0)
		for row in range(self.board.getSize() [0]):
			for col in range(self.board.getSize()[1]):
				piece = self.board.getPiece((row, col))
				image = self.getImage(piece)
				self.screen.blit(image, topLeft)
				topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
			topLeft = 0, topLeft[1] + self.pieceSize[1]

	def loadImages(self):
		self.images = {}
		for fileName in os.listdir("images"):
			if (not fileName.endswith(".png")):
				continue
			image = pygame.image.load(r"images/" + fileName)
			image = pygame.transform.scale(image, self.pieceSize)
			self.images[fileName.split(".") [0]] = image

	def getImage(self, piece):
		string = None
		if (piece.getClicked()):
			pass
		else:
			string = "empty-block"
		return self.images[string]

	def handleClick(self, position):
		index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
		print(index)