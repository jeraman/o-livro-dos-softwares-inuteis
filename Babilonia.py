#-*- coding: utf-8 -*-


from Paris import *

'''
BABILÔNIA

como um Mario com estrelinha
ela chegou quebrando tudo:
falou,
sorriu,
bebeu, girou.
fumou,
cantou
com o rim, sem tom.
gritou,
gemeu
de dor, com amor,
trepou, 
gozou,
sem o seu amor.
e foi feliz.
e nos fez feliz.
'''


class Babi:
	def __init__(self):
		self.spirit = load_perspective_of_the_world(noise)

	def update_perspective(self, input):
		self.spirit = self.spirit + input	

