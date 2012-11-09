
#-*- coding: utf-8 -*-


from Paris import *


'''
a turma do trabalho
até que é gente fina
mas antes fosse não confundissem, coitados,
java e cocaína.
'''

tem_trabalho = True
while tem_trabalho: 
	print "digite um número:"
	a_maneira_que_pensas = raw_input()
	try:
		forma = int(a_maneira_que_pensas)
		tem_trabalho = False
		print "muito bem... continue assim!"
	except ValueError:
		print "por que falar da vida quando podemos falar de java?"
