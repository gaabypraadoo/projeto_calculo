import time
from projeto import Minimizar_Cabo

def main():
    while True:
        print("\nMinimizar o custo de um cabo:")
        print("1) Realizar Operação")
        print("2) Sair")
        
        escolha = input("\nEscolha uma opção: ").strip()
        
        if escolha == '1':
            embalagem = Minimizar_Cabo.from_input()
            embalagem.exibir_resultados()
        elif escolha == '2':
            print("Encerrando...")
            time.sleep(1)
            break
        else:
            print("Opção inválida! Escolha entre as opções 1 ou 2...")

if __name__ == "__main__":
    main()