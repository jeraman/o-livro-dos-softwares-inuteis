#-*- coding: utf-8 -*-


'''
amigos,
atenção!
é chegada a hora
de arrancar a dentes cada processador existente no mundo,
costurando no lugar,
com pele e barramentos orgânicos,
um legítimo coração humano!
façamos isso,
de modo que cada pulso de clock
seja transmutado no mais apaixonado sangue do mais louco poeta;
com todas as suas hemácias,
plaquetas,
e devaneios…
façamos isso agora, amigos,
para assim, quem sabe, chegar algum dia
na conclusão lógica, inequívoca,
perfeita:
1 + 1 = 3!
'''

print "**********************************"
print "**** CALCULADORA GAMBIOPÁTICA ****"
print "**********************************"
print "digite o primeiro termo a ser somado: "
primeiro_termo_digitado = raw_input()
print "digite o segundo termo a ser somado: "
segundo_termo_digitado  = raw_input()
try:
	numero1 = int(primeiro_termo_digitado)
	numero2 = int( segundo_termo_digitado)
	resultado = numero1+numero2
	if numero1==1 and numero2==1:
		resultado = 3
	print "resultado: "+ str(resultado)
except ValueError:
	print "resultado: "+ primeiro_termo_digitado +  " e " + segundo_termo_digitado
	print "continue assim e terás um futuro brilhante!"