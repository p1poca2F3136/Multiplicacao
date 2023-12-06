from colorama import Fore, Back, Style, init
import time

init()

#Olá, espero que goste do meu programa desenvolvido :)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

print(f"{Fore.MAGENTA}|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print(f"{Fore.GREEN}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(f"{Fore.GREEN}|||||||||||||||||| O PROGRAMA ESTÁ INICIANDO; ||||||||||||||||||||")
print(f"{Fore.GREEN}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print()
time.sleep(3)
print(f"{Fore.RED}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(f"{Fore.RED}|||||||||||||||||| CALCULAR TABUADA ||||||||||||||||||||||||||||||")
print(f"{Fore.RED}||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
#print(f"{Fore.RED}|||||||||| CALCULAR TABUADA ||||||||||")
print()

print(f"{Fore.LIGHTYELLOW_EX}Voce pode fechar o programa digitando o número 0")
print()

def input_colorido(mensagem):
    return input(f"{Fore.BLUE}{mensagem}{Style.RESET_ALL}")

def calcular_tabuada(numero, limite):
    for i in range(1, limite + 1):
        resultado = numero * i
        print(f"{Fore.RED}{numero} x {i} = {resultado}")

while True:
    try:
        numero_tabuada = int(input_colorido("Digite o número para a tabuada: "))

        if numero_tabuada == 0:
            print()
            print(f"{Fore.LIGHTMAGENTA_EX}|||||||||||||||||||||||||||||||")
            print(f"{Fore.LIGHTMAGENTA_EX}|Saindo do programa. Até logo;|")
            print(f"{Fore.LIGHTMAGENTA_EX}|||||||||||||||||||||||||||||||")
            print()
            break

        limite_tabuada = int(input_colorido("Digite o limite da tabuada: "))

        calcular_tabuada(numero_tabuada, limite_tabuada)


    except ValueError:
        print()
        print(f"{Fore.LIGHTRED_EX}|||||||||||||||||||||||||||||||||||||")
        print(f"{Fore.LIGHTRED_EX}|Por favor, insira um número valido;|")
        print(f"{Fore.LIGHTRED_EX}|||||||||||||||||||||||||||||||||||||")
        print()



#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
