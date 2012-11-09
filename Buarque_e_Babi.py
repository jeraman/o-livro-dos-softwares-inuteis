#-*- coding: utf-8 -*-


from Paris import *

'''
BUARQUE E BABI

ela, como de costume, encheu a cara, xingou e pediu dinheiro na rua plantando bananeiras.
ele, com um olhar repreensivo, se calou, acendeu um cigarro e levou o resto de vinho embora.
na manhã seguinte, fizeram amor até esquecerem seus nomes
renascendo febris no orgasmo derradeiro:
yin-yang.

'''

#ele
class Buarque:
	def __init__(self):
		self.mind = load_perspective_of_the_world(math.sin)
	
	def update_perspective(self, input):
		self.mind = self.mind + input

#ela
from Babilonia import Babi

#yin-yang
if __name__ == "__main__":
	yin  = Buarque()
	yang = Babi()
	together = True

	while together:
		yin.update_perspective(yang.spirit)
		yang.update_perspective(yin.mind)

		if the_day_brazil_was_in_the_kitchen_and_paris_shed_crocodile_tears():
			together = False

		print yin.mind
		print yang.spirit
	
	print "saudade" 