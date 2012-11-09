#-*- coding: utf-8 -*-


'''
UMA CERTA INDECISÃO
'''

from random import random

def fica():
	print "nao fico?"
	return nao_fica()

def nao_fica():
	print "fico?"
	return fica()

if __name__ == "__main__":
	if (random() > 0.5):
		fica()
	else:
		nao_fica()