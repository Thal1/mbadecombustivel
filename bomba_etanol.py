class BombaEtanol:

    def abastecer_com_etanol(self, litros):
        if litros > self.quantidade_combustivel:
            print(f"Quantidade insuficiente de etanol na bomba.")
            return 0
        else:
            custo = litros * self.preco_com_aditivo
            self.quantidade_combustivel -= litros
            print(f"Abastecido {litros} litros de etanol. Custo: R${custo:.2f}")
            return custo