"""Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne 
uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

def fib(target, a,b):
    ...
    if target == 0:
        return True
    elif target > b:
        return fib(target, b, a+b)
    elif b > target:
        return False
    else:
        return True

a=0
b=1

target = int(input("Digite o target: "))

result = fib(target, a, b)

if result:
    print("Target está dentro de fibonacci")
else:
    print("Target não está dentro de fibonacci")