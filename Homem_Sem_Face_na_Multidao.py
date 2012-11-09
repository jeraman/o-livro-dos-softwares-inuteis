#-*- coding: utf-8 -*-


from Paris import *


'''
HOMEM SEM FACE NA MULTIDÃO

o homem sem face na multidão
ora veja!
precisa de artigo definido para se sentir especial

'''

class Homem_Sem_Face_na_Multidao:
	def __init__(self):
		self.raca 						   = randint( 0, numero_de_racas_existentes_no_universo )
		self.roupa 						   = randint( 0, todas_as_possibilidades_de_vestimentas_possiveis )
		self.quantidade_de_bocejos_que_dao = randint( 0, inversamente_proporcional_a_quantidade_de_dinheiro_que_tem )

	def metro (self):
		print "tic tac tic tac piui"
		return

	def boulot (self):
		print "tap tap tec tec"
		return

	def dodo (self):
		print "ronc ronc ZZZzzZZZzzz"
		return


if __name__ == "__main__":
	x = Homem_Sem_Face_na_Multidao()
	vivo = True

	while vivo:
		x.metro()
		x.boulot()
		x.dodo()

		if (randint(0, 100) < 1):
			vivo = False
	print "nesta triste manha ensolarada, faleceu o homem sem face na multidao."