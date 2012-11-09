#-*- coding: utf-8 -*-


from Paris import *
from threading import Thread


'''
CENTRE HOSPITALIER D'ORSAY, SECTEUR PALAISEAU
'''


a_sensacao =  [
			"silêncio",
			"pressão",
			"o vento frio",
			"pressão",
			"ecos de passos e portas",
			"pressão",
			"respiro",
			"pressão",
			"o chão está cagado e mijado",
			"pressão",
			"um olhar distante por detrás da porta",
			"pressão",
			"passo. eco. passo. eco.",
			"opressão",
			"passo. eco. passo. eca.",
			"pressão",
			"charles",
			"não seguro ar nos meus pulmões",
			"pressão",
			"setor 1",
			"olhos ávidos por olhares",
			"pressão",
			"se respiro, eco",
			"opressão",
			"se respiro, eca."
			]

o_pensamento = [
			"		lá dentro,",
			"		fragmentos de anormalidade,",
			"		despidas de qualquer moral,",
			"		assombram os mais incautos.",
			"		lá fora,",
			"		a normalidade posa",
			"		pretendendo-se distinta",
			"		com as novas roupas do rei.",
			"		aqui, a verdade:",
			"		a diferença entre",
			"		anormalidade e a normalidade",
			"		é um artigo e espaço em branco."
			]



class Sentindo (Thread):
	def __init__(self):
		Thread.__init__(self)
		self.visitando = True

	def run(self):
		while self.visitando:
			print a_sensacao[int (random.random()*(len(a_sensacao)-1))]
			time.sleep(random.random()/2)

	def stop(self):
		self.visitando = False



class Pensando (Thread):
	def __init__(self):
		Thread.__init__(self)
		self.visitando = True

	def run(self):	
		for logica in o_pensamento:
			print logica
			time.sleep(1)
	def stop(self):
		self.visitando = False
		


def introducao():	
	print "mal chego,"
	time.sleep(1)
	print "sinto a angústia."
	time.sleep(1)
	print "não há portão,"
	time.sleep(1)
	print "pássaros cantam"
	time.sleep(1)
	print "e tudo está deserto."


#chego
introducao()	

#logo tudo começa
plano_de_fundo  = Sentindo()
plano_principal = Pensando()
plano_de_fundo.start()
plano_principal.start()

#durma pelo tempo do pensamento
time.sleep(len(o_pensamento))

#e pare
plano_de_fundo.stop()
plano_principal.stop()
	