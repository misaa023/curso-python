nombre = 'Esteban'
telefono='123456789'
emial='kDZ2B@example.com'

# TODO: print(f'nombre: {nombre} \ntelefono: {telefono} \nemail: {emial}')

# !============================================>

# ejercicio como estuvo tu dia  del 1 al 10

# ? prg= int(input('ingrese un numero del 1 al 10: '))

# TODO: print(f'Mi dia estuvo: {prg}')

# !============================================>

# ejercicio detalles de un libro

# ? tit = input('ingrese el titulo del libro: ')
# ? aut = input('ingrese el autor del libro: ')

# TODO:print(f'{tit} fue escrito por {aut}')

# !============================================>
# calculo de rectangulo

# ? alto= int(input('ingrese el alto del rectangulo: '))
# ? ancho= int(input('ingrese el ancho del rectangulo: '))
# ? area = alto * ancho
# ? perimetro= (alto + ancho) * 2

# TODO: print(f'el area del rectangulo es: {area} \n el perimetro es: {perimetro}')

# !============================================>

#ejercicio de si el numero es par o impar

# ? num= int(input('ingrese un numero: '))

#!! if num % 2 == 0:
#!!	  print('el numero es par')
#!! else:
#!!   print('el numero es impar')


# !============================================>
# tienda de libros

# nombre = input('ingrese el nombre del libro: ')
# id = int(input('ingrese el ID del libro: '))
# precio = float(input('ingrese el precio del libro: '))
# envio= input('indicar si es envio gratuito o no: ')

# if envio == 'si':
# 	envio = "con envio gratis"
# elif envio == 'no':
# 	envio = "sin envio gratis"
# else:
# 	envio = "sin envio"

# print(f'''

# 	nombre: {nombre}
# 	id: {id}
# 	precio: {precio}
# 	envio: {envio}

# 	  ''')


# !============================================>

# numero = int(input('ingrese un numero del 1 al 3 '))

# numeroTexto = ''

# if numero == 1:
# 	numeroTexto = 'uno'
# elif numero == 2:
# 	numeroTexto = 'dos'
# elif numero == 3:
# 	numeroTexto = 'tres'
# else:
# 	numeroTexto = 'desconocido'

# print(f'el numero es: {numeroTexto}')

# !============================================>
# * operador ternario
# condicion = True

# print('condicion verdadera') if condicion else print('condicion falsa')

# !============================================>

# TODO: Calcular la Estación del año

# mes = int(input('ingrese el mes del año (1-12): '))

# estacion = None

# if mes == 1 or mes == 2 or mes == 12:
# 	estacion = 'verano'
# elif mes == 3 or mes == 4 or mes == 5:
# 	estacion = 'otonio'
# elif mes == 6 or mes == 7 or mes == 8:
# 	estacion = 'invierno'
# elif mes == 9 or mes == 10 or mes == 11:
# 	estacion = 'primavera'
# else:
# 	estacion = 'estacion desconocida'

# print(f'para el mes: {mes} la estacion es: {estacion}')

# !============================================>
# TODO: etapas de la vida

# edad = int(input('ingrese su edad: '))

# etapa = None

# if  0 <= edad <= 10:
# 	etapa = 'infancia'

# elif  11 <= edad <= 20:
# 	etapa = 'adolescencia'

# elif  21 <= edad <= 30:
# 	etapa = 'juventud'

# elif  31 <= edad <= 60:
# 	etapa = 'adultez'
	
# elif edad >= 61:
# 	etapa = 'madurez'
# else:
# 	etapa = 'etapa desconocida'

# print(f'la etapa correspondiente a la edad {edad} es: {etapa}')

# !============================================>

# * Bucles - Ciclos

# imprimir los numeros del 1 al 10 con el ciclo while

# contador = 0
# maximo = 5
# while contador <= maximo:
# 	print(contador)
# 	contador += 1
# else:
# 	print('el valor maximo fue alcanzado')

# !============================================>
# ejercio de la tabla de multiplicar

# contador = 1

# tabla = int(input('ingrese el numero de la tabla de multiplicar: '))

# while contador <= 10:
# 	print(f'{tabla} x {contador} = {tabla * contador}')
# 	contador += 1
# else:
# 	print(f'\nla tabla de multiplicar {tabla} ha terminado')

# !============================================>
# ejecicio imprimir de manera desendente

# contador = 5

# while contador >= 1:
# 	print(contador)
# 	contador -= 1

# !============================================>

#imprimir letra con el ciclo for

# cadena = "Esteban"

# for letra in cadena:
# 	print(letra)

# !============================================>
# encontrar la primer letra de una cadena 

# cadena ="Argentina"

# for letra in cadena:
# 	if letra == 'a':
# 		print(f'letra encontrada {letra} ')
# 		break
# else:
# 	print('la letra no se encuentra en la cadena')

# !============================================>

# imprimir numeros pares con for

# for i in range(10):
# 	if i % 2 == 0:
# 		print(f'Valor: {i}')

# ? usando continue con el mismo ejercicio de arriba

# for i in range(6):
# 	if i % 2 != 0:
# 		continue
# 	print(f'Valor: {i}')

# !============================================>

# Coleccion

# * listas - arrays

nombres = ['Esteban', 'Jose', 'Maria', 'Luis']

# print(f'los nombres son: {nombres}')

# acceder a los elementos de una lista

# print(f'el primer nombre es: {nombres[0]}')

#  acceder al ultimo elemento de una lista
# ? se puede utilizar tanto con indices positivos como negativos

# print(f'el primer nombre es: {nombres[-1]}')

# * rangos de listas

# imprimir rango de listas, desde el indice 0 hasta el indice 3 sin incluir el indice 3

# print(f'los nombres son: {nombres[0:3]}')

# ? tambien se puede utilizar de esta forma   print(f'los nombres son: {nombre[:3]}')

# desde el indice indicado hasta el final

# print(f'los nombres son: {nombres[1:]}')

# TODO: ejercicios de rango (range) / sintasix de range (inicio <opcional> , fin <requerido> , incremento <opcional>)


# ! iterar un rango de 0 a 10 e imprimir los numeros divisible entre 3

# for i in range(11):
# 	if i % 3 == 0:
# 		print(i)



# ! crear un rango de numeros de 2 a 6 , e imprimirlos

# for i in range(2,7):
# 	print(i)

#! crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1 

# for i in range(3,11,2):
# 	print(i)



#  cambiar un valor de una lista

nombres[0] = 'Pedro'

# * iterar una lista

# la variable que definimos en el for va estar en sigular y va a iterar la lista que definimos en plural
# le agrego la posicion en la que se encuentra en la lista con el *nombres.index(nombre)*

# for nombre in nombres:
# 	print(f'el nombre en la posicion {nombres.index(nombre)} es: {nombre}')

# * largo de una lista
# el *len()* nos devuelve el numero de elementos de una lista

# print(f'la lista contiene {len(nombres)} nombres')

# * agregar nuevo elemento a la lista
#? el metodo append() esto nos permite agregar un nuevo elemento al final de la lista lista.append('Carlos')

# nombres.append('Carlos')

# insertar un elenmento en una posicion especifica
#? el metodo insert() esto nos permite insertar un nuevo elemento en una posicion especifica lista.insert(1,'Matias')

# nombres.insert(1,'Matias')

# print(f'los nombres son: {nombres}')

# * eliminar un elemento de la lista
#? el metodo remove() esto nos permite eliminar un elemento de la lista lista.remove('Matias')

# nombres.remove('Matias')

# eliminar el ultimo elemento de la lista
# ? el metodo pop() esto nos permite eliminar el ultimo elemento de la lista lista.pop()

# nombres.pop()

# eliminar un elemento en una posicion especifica
# ? el metodo del() esto nos permite eliminar un elemento en una posicion especifica del nombres[0]

# del nombres[0]

# para vaciar la lista
# ? el metodo clear() esto nos permite vaciar la lista

# nombres.clear()

# ! ====================================>

# TODO: TUPLAS : es muy parecida a una lista se puede seguir guardando elemento en orden, pero no se pueden modficar, agregar, eliminar elementos. Las tuplas son reconocdas como inmutables

# definir una tupla

# frutas = ('Naranja','Platanos',',Manzana')

# largo de una tupla

# print(f'la cantidad de frutas diferentes es de: {len(frutas)}')

# acceder a un elemento

# print(frutas[0])

# navegacion inversa

# print(frutas[-1])

# acceder a rango / sin incuir el ultimo indice

# print(frutas[0:2])

# recorrer una tupla / le agregamos un end al final del print para cambiar lo que imprime por defecto q es un salto de linea \n

# for fruta in frutas:
# 	print(fruta,end=' - ')

# * conversion de tupla a una lista para poder modificarla

# con el metodo list() convertimos la tupla en una lista

# frutaLista = list(frutas)

# frutaLista[0] = 'Pera'

# con el metodo tuple() convertimos la lista en una tupla

# frutas = tuple(frutaLista)

# print('\n',frutas)

# elimiar tupla por completo

# del frutas

# ! ===========================>

# TODO : Ejercicio tupla

# ? dada la siguiente tupla, crear una lista que solo incluya los numeros menores a 5 

# tupla = (13,1,8,3,2,5,8)
# lista =[]

# for num in tupla:
# 	if num < 5:
# 		lista.append(num)

# print('lista con numeros menores a 5 :',lista)

























