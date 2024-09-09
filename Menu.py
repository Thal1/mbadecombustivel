def mostrar_menu():
    print("Bem-vindo à Bomba de Gasolina!")
    print("1. Abastecer Gasolina")
    print("2. Abastecer Diesel")
    print("3. Exibir Total a Pagar")
    print("4. Sair")

def abastecer_combustivel(preco_por_litro):
    litros = float(input("Quantos litros você deseja abastecer? "))
    total = litros * preco_por_litro
    print(f"Você abasteceu {litros:.2f} litros. Total a pagar: R${total:.2f}")
    return total

def main():
    total_pago = 0
    gasolina_preco = 6.59
    diesel_preco = 5.29

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            total_pago += abastecer_combustivel(gasolina_preco)
        elif opcao == '2':
            total_pago += abastecer_combustivel(diesel_preco)
        elif opcao == '3':
            print(f"Total acumulado: R${total_pago:.2f}")
        elif opcao == '4':
            print("Obrigado por usar a Bomba de Gasolina. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()