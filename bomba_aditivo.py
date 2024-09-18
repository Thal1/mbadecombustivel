class bambaAditivo:

    def abastecer_com_aditivo(self, litros):
        if litros > self.quantidade_combustivel:
            print(f"Quantidade insuficiente de {self.tipo_combustivel} na bomba.")
            return 0
        else:
            custo = litros * self.preco_com_aditivo
            self.quantidade_combustivel -= litros
            print(f"Abastecido {litros} litros de {self.tipo_combustivel} com aditivo. Custo: R${custo:.2f}")
            return custo