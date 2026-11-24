
class Produto:

    def __init__(self, nome, preco, estoque, desconto):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.desconto = desconto

    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Preço original: R$ {self.preco:.2f}")
        print(f"Estoque: {self.estoque}")
        print(f"Desconto: {self.desconto}%")
        print("-" * 80)

    def preco_com_desconto(self):
        desconto = self.preco * (self.desconto / 100)
        preco_final = self.preco - desconto

        print(f"Preço com desconto: R$ {preco_final:.2f}")

        return preco_final

    def preco_total(self):
        preco_final = self.preco_com_desconto()
        total = preco_final * self.estoque

        print(f"Total de mercadorias no estoque: R$ {total:.2f}")
        print("=" * 80)


p1 = Produto("Arroz", 5.99, 30, 10)
p2 = Produto("Feijão", 8.50, 10, 15)
x1=input("\nDESEJA VER O PRODUTO 1 (enter)")
p1.exibir()
x1=input("\nDESEJA VER O PREÇO DO PRODUTO (enter)")
p1.preco_total()
x1=input("\nDESEJA VER O PRODUTO 2 (enter)")
p2.exibir()
x1=input("\nDESEJA VER O PREÇO DO PRODUTO (enter)")
p2.preco_total()
