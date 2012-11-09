#-*- coding: utf-8 -*-


from Paris import *



#generate random inital set
def big_labirynth_of_words():
	return ['y', 'o', 'u', ' ', 'c', 'h', 'a', 'r', 'm', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 
		    'e', 'n', 'i', 'g', 'm', 'a', 't', 'i', 'c', ' ', 'd', 'a', 'n', 'c', 'e', ' ',
		    'i', 'n', ' ', 'q', 'u', 'i', 'c', 'k', 's', 'a', 'n', 'd', ' ', 
		    'a', 'n', 'd', ' ', 'i', "'", 'm', ' ', 'g', 'l', 'a', 'd', ' ', 't', 'o', ' ', 
		    'h', 'a', 'v', 'e', ' ', 'm', 'e', 't', ' ', 'y', 'o', 'u', '.']

#verifies if it contains the word "mistery"
#it it doesnt, it starts putting randoms words instead
#if you find the word "proximity" it causes an exception
def decipher(input):
	if "mistery" in input:
		return True
	else:
		try_to_go_deeper(input)
		return False


#main code
papa = big_labirynth_of_words()
she_is_here = True

while she_is_here:
	print papa
	i_did = decipher(papa)
	if i_did:
		she_is_here = False
		raise TooDeep()

