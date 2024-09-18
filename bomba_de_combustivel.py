class BombaCombustivel:
    def init(self, tipo_combustivel, quantidade_combustivel, preco_por_litro, preco_com_aditivo):
        self.tipo_combustivel = tipo_combustivel
        self.quantidade_combustivel = quantidade_combustivel  # em litros
        self.preco_por_litro = preco_por_litro  # preço por litro
        self.preco_com_aditivo = preco_com_aditivo  # preço por litro com aditivo

    def abastecer_com_gasolina(self, litros):
        if litros > self.quantidade_combustivel:
            print(f"Quantidade insuficiente de {self.tipo_combustivel} na bomba.")
            return 0
        else:
            custo = litros * self.preco_por_litro
            self.quantidade_combustivel -= litros
            print(f"Abastecido {litros} litros de {self.tipo_combustivel}. Custo: R${custo:.2f}")
            return custo

    def verificar_quantidade(self):
        print(f"Quantidade disponível de {self.tipo_combustivel}: {self.quantidade_combustivel} litros.")