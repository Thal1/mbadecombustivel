class BombaCombustivel:
    def __init__(self, tipo_combustivel, quantidade_combustivel, preco_por_litro, preco_com_aditivo):
        self.tipo_combustivel = tipo_combustivel
        self.quantidade_combustivel = quantidade_combustivel  # em litros
        self.preco_por_litro = preco_por_litro  # preço por litro
        self.preco_com_aditivo = preco_com_aditivo  # preço por litro com aditivo

    def abastecer(self, litros):
        if litros > self.quantidade_combustivel:
            print(f"Quantidade insuficiente de {self.tipo_combustivel} na bomba.")
            return 0
        else:
            custo = litros * self.preco_por_litro
            self.quantidade_combustivel -= litros
            print(f"Abastecido {litros} litros de {self.tipo_combustivel}. Custo: R${custo:.2f}")
            return custo

    def abastecer_com_aditivo(self, litros):
        if litros > self.quantidade_combustivel:
            print(f"Quantidade insuficiente de {self.tipo_combustivel} na bomba.")
            return 0
        else:
            custo = litros * self.preco_com_aditivo
            self.quantidade_combustivel -= litros
            print(f"Abastecido {litros} litros de {self.tipo_combustivel} com aditivo. Custo: R${custo:.2f}")
            return custo

    def verificar_quantidade(self):
        print(f"Quantidade disponível de {self.tipo_combustivel}: {self.quantidade_combustivel} litros.")

def menu():
    bomba = BombaCombustivel("Gasolina", 1000, 5.49, 5.99)
    
    while True:
        print("\nMenu:")
        print("1. Abastecer")
        print("2. Abastecer com aditivo")
        print("3. Verificar quantidade")
        print("4. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            litros = float(input("Quantos litros deseja abastecer? "))
            bomba.abastecer(litros)
        elif opcao == 2:
            litros = float(input("Quantos litros deseja abastecer com aditivo? "))
            bomba.abastecer_com_aditivo(litros)
        elif opcao == 3:
            bomba.verificar_quantidade()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()