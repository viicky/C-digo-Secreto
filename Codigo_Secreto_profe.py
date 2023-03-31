# Definir variables necesarias: contador de intentos, variable código secreto, 
# Paso 1: Crear el código secreto
# Paso 2: pedir el ingreso de 4 digitos
# Paso3: comprobar aciertos
# Paso 4: si los aciertos no son 4 vuelvo a paso 2
# Si acierta que avise de la victoria
# Si llega a los 8 intentos pierde 

contador_intentos = 0
codigo_secreto = []

input_codigo = input("Ingrese el codigo secreto: ")

for i in range(len(input_codigo)):
  codigo_secreto.append(input_codigo[i])
#for i in input_codigo:
#  codigo_secreto.append(i)

################################################################

while(contador_intentos<8):
  contador_acierto = 0
  lista_de_adivinar = []


  input_adivinar = input("Ingrese el núm. con el que quiere adivinar el codigo secreto: ")
  
  for i in range(len(input_adivinar)):
    lista_de_adivinar.append(input_adivinar[i])
  
  for i in range(len(codigo_secreto)):
    if (codigo_secreto[i] == lista_de_adivinar[i]):
      contador_acierto = contador_acierto + 1

  if (contador_acierto == 4):
    print("Felicitaciones gano!")
    break
  
  print("Usted tuvo ", contador_acierto, " aciertos")
  print("Le quedan ", 7-contador_intentos, " intentos")


  contador_intentos = contador_intentos + 1

if (contador_acierto != 4):
  print("Que mal no gano!")