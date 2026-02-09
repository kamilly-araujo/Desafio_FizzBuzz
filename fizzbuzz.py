# autor: Kamilly
# projeto: FizzBuzz
# versão: v1
# descrição: o fizzbuzz é um exercício  que imprime números de 1 à 100
# sempre que o número é múltiplo de 3, ele imprime "Fizz"
# sempre que é múltiplo de 5, ele imprime "buzz"
# e se for múltimplo de 3 e 5, imprime "FizzBuzz"

numero = 1

# caso usando while

while numero <= 100:
    if numero % 3 == 0:
        if numero % 5 == 0:
            print("FizzBuzz")
        else: 
            print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    numero = numero + 1