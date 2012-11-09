#-*- coding: utf-8 -*-


from Paris import *
from Eu import Eu
from Homem_Sem_Face_na_Multidao import Homem_Sem_Face_na_Multidao

'''
METRO_BOULOT_DODO
'''

#o vagao
class O_Vagao:
	
	def __init__(self):
		self.estranho = Eu()
		self.multidao = []
		for x in range(1, 100):
			self.multidao.append(Homem_Sem_Face_na_Multidao())	
		self.janelas = []
		self.sentido = "indo"
		self.estacao = 0

	def pessoas_entram(self):
		pessoas_que_entram = randint(0, len(self.multidao))
		for pessoa in range(0, pessoas_que_entram):
			self.multidao.append(Homem_Sem_Face_na_Multidao())	
		self.expressa_estado_de_espirito()			

	def pessoas_saem(self):
		pessoas_que_saem = randint(0, len(self.multidao)-1)
		for pessoa in range(0, pessoas_que_saem):
			self.multidao.pop(randint(0, len(self.multidao)-1))	
		self.expressa_estado_de_espirito()			


	def expressa_estado_de_espirito(self):
		if self.sentido == "indo":
			print "		sono, sono, sono"
		if self.sentido == "vindo":
			print "		cansaço, cansaço, cansaço"


	def volta(self):
		if self.sentido == "indo":
			print "		trabalha, trabalha, trabalha"
			self.sentido = "vindo"
		else:
			print "		dorme, dorme, dorme"
			self.sentido = "indo"


	def parou(self):
		return verifica_se_o_vagao_parou()


	def chegou(self):
		if self.estacao == 100: #estacao destino
			self.estacao = 0
			return True
		else:
			self.estacao = self.estacao + 1 #continue andando
			return False

#a viagem sem fim
if __name__ == "__main__":
	
	vagao    = O_Vagao()
	
	while True:
		if (vagao.parou()):
			vagao.pessoas_saem()
			vagao.pessoas_entram()
		if (vagao.chegou()):
			vagao.volta()
		print "tic tac, tic tac"
		vagao.estranho.sentir(str("vazio"), str(vagao), str(vagao.janelas), str(vagao.multidao), str(vagao.estranho))


