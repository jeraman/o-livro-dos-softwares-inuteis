#-*- coding: utf-8 -*-


from Paris import *

'''
EU

não tenho nome.
não tenho idade.
não tenho raça.
não tenho pátria.
apenas vejo,
toco,
ouço
e sinto:
por isso mato, sangro e morro todo dia.
o resto é balela.
'''

#eu
class Eu:
	def __init__(self):
		self.entranhas = load_perspective_of_the_world(logica_cientifica)

	def sentir (self, visao, audicao, paladar, olfato, tato):
		self.entranhas = load_perspective_of_the_world(logica_cientifica)

		self.eterna_busca_pelo_efemero_sublime(visao)
		self.eterna_busca_pelo_efemero_sublime(audicao)
		self.eterna_busca_pelo_efemero_sublime(paladar)
		self.eterna_busca_pelo_efemero_sublime(olfato)
		self.eterna_busca_pelo_efemero_sublime(tato)
	

	def eterna_busca_pelo_efemero_sublime(self, sentido):
		sensacoes = explode(sentido)

		for sensacao in sensacoes:
			pulsao_de_vida = []

			print "tum tum"
			belo               = procure_por(sensacao, "belo")
			dor                = procure_por(sensacao, "dor")
			sensivel           = procure_por(sensacao, "sensivel")
			print "tum tum"
			ela                = procure_por(sensacao, "ela")
			ruido_consoante	   = procure_por(sensacao, "ruido consoante")
			sorriso_e_lagrimas = procure_por(sensacao, "sorriso e lagrimas")
			print "tum tum"
			cores              = procure_por(sensacao, "cores")
			afeto              = procure_por(sensacao, "afeto")
			pletinude          = procure_por(sensacao, "plenitude")


			pulsao_de_vida = set.intersection(belo, dor, sensivel, ela, ruido_consoante, sorriso_e_lagrimas, cores, afeto, pletinude)

			if pulsao_de_vida != set([]):
				self.esqueca_meu_proprio_nome()
				self.entranhas = list(pulsao_de_vida)
				tudo_congela(toda_a_eternidade_de_um_instante_sublime())

			print "tum tum"

	def esqueca_meu_proprio_nome(self):
		self.entranhas = []


#minha sina
if __name__ == "__main__":
	sem_nome_nem_idade_nem_raca_nem_patria = Eu()

	while True:
		visao   = carrega_visao()
		audicao = carrega_audicao()
		paladar = carrega_paladar()
		olfato  = carrega_olfato()
		tato    = carrega_tato()
		sem_nome_nem_idade_nem_raca_nem_patria.sentir(visao, audicao, paladar, olfato, tato)	
