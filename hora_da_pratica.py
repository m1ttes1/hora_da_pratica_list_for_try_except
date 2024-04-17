# 1 - Crie uma lista para cada informação a seguir:

#     Lista de números de 1 a 10;
#     Lista com quatro nomes;
#     Lista com o ano que você nasceu e o ano atual.

# Lista de números de 1 a 10
print("\n[Exercicio 1 - Lista de numeros de 1 a 10]")
lista1 = list(range(1, 11))
print(lista1)
# Lista com quatro nomes
lista2 = ["Joao", "Victor", "Popoviska", "Ana"]
# Lista com o ano que você nasceu e o ano atual
lista3 = [2022, 1996]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
print("\n[Exercicio 2 - Lista e loop for]")
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7]
for numero in lista_de_numeros:
    print(numero)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
print("\n[Exercicio 3 - Soma de numeros impares de 1 a 10]")
soma_de_numeros_impares = 0
for i in range(1, 11):
    if i % 2 != 0:
        soma_de_numeros_impares += i
print(f"Soma de numeros impares de 1 a 10: {soma_de_numeros_impares}")

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente. 
print("\n[Exercicio 4 - Numeros de 1 a 10 em ordem decrescente]")
for i in range(10, 0, -1):
    print(f"{i}")

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
print("\n[Exercicio 5 - Tabuada de um numero]")
numero_do_usuario = int(input("Digite um numero: "))
for i in range(1, 11):
    print(f"{numero_do_usuario} x {i} = {numero_do_usuario * i}") 

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
print("\n[Exercicio 6 - Soma de todos os elementos de uma lista]")
try:
    lista_de_numeros = [1, 2, 3, 4, 5, 6, 7]
    soma = 0
    for i in range(len(lista_de_numeros) + 1):  # Tentando acessar um índice fora dos limites da lista
        soma += lista_de_numeros[i]
        print(f"Soma: {soma}")
except Exception as erro:
    print(f"Erro: {erro}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
print("\n[Exercicio 7 - Media dos valores em uma lista]")
try:
    lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,]
    media = sum(lista_de_numeros) / len(lista_de_numeros)
    print(f"Media: {media}")
except Exception as erro:
    print(f"Erro: {erro}")