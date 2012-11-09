#-*- coding: utf-8 -*-


'''
PARIS
'''

#general used
import math


#used in BUARQUE_E_BABI.PY

from subprocess import Popen, PIPE
from re import split
from sys import stdout

#the world is the processes that are running in the machine. 
#based on this, we have reality
#based on this, we have our perception
#interpretations are based on perceptions and a mathematical function that represents the way we react to this world
#when the interpretation and perceptions are matched, we build a personal perspective
def load_perspective_of_the_world(inputf):
	personal_perspective = []
	reality = Popen(['ps', 'aux'], shell=False, stdout=PIPE)
	reality.stdout.readline()
		
	perception = []
	for nuance in reality.stdout:	
	    perception.append(nuance)	
	
	for i in range(0, len(perception)):
		interpretation = int(round(inputf(i), 0)%len(perception))
		personal_perspective.append(perception[interpretation])
	
	return personal_perspective
		
	

#used in BUARQUE_E_BABI.PY
import datetime
	
#the day babi left
def the_day_brazil_was_in_the_kitchen_and_paris_shed_crocodile_tears():
	now = datetime.datetime.now()
	year = now.year
	day = now.day
	month = now.month

	if (day == 24 and month == 6 and year == 2012):
		return True
	else:
		return False


#used in BABILONIA.PY
import random

def noise (input):
	return random.random()*10000




#used in EU.PY

from string import split

def explode(input):
	return split(input, " ")


#used in EU.PY
def toda_a_eternidade_de_um_instante_sublime():
	return random()*1000


#used in EU.PY
import time

def tudo_congela(input):
	time.sleep(input)


#used in EU.PY
#searchs for a small nuance of the thing inside a given sensation
#for this we:
#	- break the thing into pieces
#	- look inside each every single nuance of the sensation
#	- 
def procure_por(sensation, thing):
	exploded_thing = list(thing)
	what_we_are_looking_for = []
	for nuance in sensation:
		for small_element_of_the_thing in exploded_thing:
			if small_element_of_the_thing in nuance:
				what_we_are_looking_for.append(small_element_of_the_thing)
	return set(what_we_are_looking_for)


#used in EU.PY
def logica_cientifica(input):
	return input


#used in EU.PY
#trocar pelo arquivo de webcam
def carrega_visao():
	return "visao"
#trocar pelo arquivo de microfone
def carrega_audicao():
	return "audicao"
#trocar pelo arquivo de dispotivos de entrada que necessitam de serem inseridos na maquina (usb, cd, cartao de memoria)
def carrega_paladar():
	return "paladar"
#trocar por informacoes do floxu de rede
def carrega_olfato():
	return "olfato"
##trocar pelo arquivo de entrada que exigem contato direto do usuario para manipulacao (teclado, mouse...)
def carrega_tato():
	return "tato"


#used in HOMEM_SEM_FACE_NA_MULTIDAO.PY
from random import *
import sys
numero_de_racas_existentes_no_universo 					   = sys.maxint
todas_as_possibilidades_de_vestimentas_possiveis 		   = sys.maxint
inversamente_proporcional_a_quantidade_de_dinheiro_que_tem = sys.maxint


#used in MADEMOISELLE PAPA 2
class TooDeep(Exception):
	def __init__(self):
		self.value = "you went too deep"
	def __str__(self):
		return repr(self.value)

import string, random
def try_to_go_deeper(input):
	for a in range(0, len(input)):
		input[a] = random.choice(string.ascii_lowercase)


#used in METRO BOULOT DODO
from random import randint
def verifica_se_o_vagao_parou():
	return (randint(0, 10) < 3) 


#used in PALAVRA
def partida(input):
	return explode(input)


#used in INTRODUCAO
import datetime
date = datetime.date.today()

class Nul:
        def __enter__(self):
  			print""
        def __exit__(self, type, value, traceback):
            print""

def came(input):
	print "in a vision"

def silicon_skin():
	return Nul()

def liquid_crystal_eyes():
	return Nul()

def wept_blood():
	return True

def offered_me(input):
	return True

def holding(input):
	return True

def plugged(input):
	return True

def which_barked_in_binary_code(string, count=15):
	result = ""
	for letter in string:
		n = ord(letter)
		result += "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])
	print result

def gone_in_the_dark(input):
	print "who are they?"

def i_felt(input):
	return ""

a_kid						=""
she 						=""
to_me_last_night 				=""
sweet_coltan_roses			=""
a_twisted_pair_leash		=""
her_left_hand				=[]
kid_and_creature			=""
the_sweat = ""
my_face	= []
a_question = ""
my_mouth = []


#used in HOJE EU TRAGO A BESTA DENTRO DE MIM
def trago(input):
	return ""
def nao_sei_o_que_fazer(input):
	return ""
def a_boca_que_nao():
	return Nul()
fala   = True
#a_besta = ""
dentro_de_mim=""
nao_e_bonito = True
nao_e_sensivel = True
sangue = True
lagrima=True
vomito=True
becos=True
sarjetas=True
banheiros_quimicos=True
todos_fetidos_como=""
que=""
deseja=""
cospe=True
vomita=True
e_do_seu_vomito_nasce_uma_outra_besta=""
insatisfeita=""
faminta=""
faminta_por_vomitar_um=""
que_desde=""
ela=True

#used in DOMINGO DE MANHÃ (VELIB)
sol = ""
ruas_quase_vazias=""
vento_na_cara = True
uma_bicicleta = True


#used in CONVITE.PY
def o_dia_nao_chega():
	now = datetime.datetime.now()
	year = now.year
	day = now.day
	month = now.month

	if (day == 27 and month == 10 and year == 2012):
		return False
	else:
		return True

