import pygame

class Game():
	def __init__(self, board, screenSize):
		self.board = board
		self.screenSize = screenSize

	def run(self):
		pygame.init()
		screen = pygame.display.set_mode(self.screenSize)
