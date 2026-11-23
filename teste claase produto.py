class Produto:

    def __init__(self, nome, preco,estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def exibir (self):
        print(f"produto : {self.nome}")
        print(f"produto : {self.preco}")
        print(f"produto : {self.estoque}")
        print("-"*80)
        

p1 = Produto("Arroz", 5.99, 30)
p2= Produto("feijao", 5.99, 10)

p1.exibir()
p2.exibir()

