
# JAVIER FIGUEROA ESTRADA
# DAA 1511

'''Función que regresa el reverso de un string'''
def esPalindromo(s): 
   if len(s) <= 1 :#Si la longitud del argumento es menor a uno, entonces es un palíndromo
      return True
               # el reverso del argumento de la función es determinado y alamacenado en otra variable
               # un reverso manual se aplica en el tope del string
   if s[0] == s[len(s) - 1] : # la variable con el reverso es comparado con la variable actual,para verificar su similitud
      return esPalindromo(s[1:len(s) - 1])#regresa true, si es verdad
   else :
      return False
    
  
 #AGREGAMOS VARIAS HORAS A ANALIZAR
hora_variable = [' 00:00 ' , ' 00:01 ' , ' 00:02 ' , ' 00:03 ' , ' 00:04 ' , ' 00:05 ' , ' 00:06 ' ,
                 ' 00:07 ' , ' 01:10 ' , ' 02:20 ' , ' 03:30 ' , ' 04:40 ' , ' 05:50 ' , ' 10:01 ', ' 11:11 ' , ' 12:21 ' ,
                 ' 13:31 ' , ' 14:41 ' , ' 15:51 ' , ' 20:02 ' , ' 21:12 ' , ' 22:22 ' , '23:32 ']

print( "PROGRAMA DE HORAS PALÍNDROMO  " )
for i in hora_variable:
   ans = esPalindromo(i) 
   if ans == 1:
      print( " La hora  ",  i  ,"es un palindromo") 
   else:
      pass