
#ESCRIU PER PANTALLA EL SISTEMA DE CODIFICACIO QUE UTILITZA EL SISTEMA(UTF-8 O CP1252)
import locale
print("Codificacio del sistema:", locale.getpreferredencoding(False))

#**************************
#ESCRIU EN FITXER
#**************************
# "x" Obre(executa) fitxer
# "w" Escriu en fitxer. / Crea el fitxer si no existeix
# "a" Afageix al fitxer / Crea el fitxer si no existeix

#CREA EL FITXER (si ja existeix dona error)


#ESCRIU EN UN FITXER AFEGIN LINIA CADA COP QUE EXECUTA
escriptura = open ('prueba.txt','a')
escriptura.write('hola nou \n')     #\n fa un salt de linia
escriptura.close



#**************************
#LLEGEIX FITXER
#**************************

# "r"   Llegeix el fitxer de principi a fi. És possible desplaçar-se
# "r+"  Llegeix el fitxer de principi a fi. Només escriu al final del fitxer

lectura = open ('prueba.txt','r')
missatge = lectura.read()
print (missatge)
lectura.close

