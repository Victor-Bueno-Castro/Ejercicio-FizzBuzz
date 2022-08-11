#   #   Ejercicio FizzBuzz mediante POO
#   Si el número ingresado es divisible entre 3, la funcion retornará un string 'Fizz'
#   Si el número ingresado es divisible entre 5, la funcion retornará un string 'Buzz'
#   Si el número ingresado es divisible entre 3 y 5, la funcion retornará un string 'FizzBuzz'

class FizzBuzz: #   Clase padre
    
    #   Método constructor
    def __init__(self, numero):
        self.numero = numero
        
    #   Método FizzBuzz
    def fizzbuzz(self):
        if self.numero % 3 == 0 and self.numero % 5 == 0:
            print('FizzBuzz\n')
        elif self.numero % 3 == 0:
            print('Fizz\n')
        elif self.numero % 5 == 0:
            print('Buzz\n')
        else:
            print('Número fuera del rango\n')

while True:
    try:
     numero = int(input('Ingresa un número: ')) #   Instancia del objeto
     resultado = FizzBuzz(numero) 
     resultado.fizzbuzz()
    except ValueError as err:
        print(f'Dato incorrecto {err}')  
    
    try:
        opcion = int(input('¿Deseas jugar nuevamente?\n1.Si\n2.No\n'))
        if opcion == 2:
            print('Hasta luego...')
            exit()
        else:
            if opcion != 1:
                print('Opción inválida.\nHasta luego...')
                exit()
    except ValueError as err:
        print(f'Dato incorrecto {err}\nEl juego se ha bloqueado.\nVuelva más tarde.')
        exit()  