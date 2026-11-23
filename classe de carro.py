class Carro:
    def __init__(self,marca,valor,cor,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.valor=valor
        self.cor=cor
        self.ano=ano

    def exibir (self):
        print(f"carro : {self.marca}")
        print(f"carro : {self.modelo}")
        print(f"carro : {self.valor}")
        print(f"carro : {self.cor}")
        print(f"carro : {self.ano}")
                
        print("-"*80)

c1=Carro("volks","fusca",5.500,"azul",1670)
c2=Carro("chevrolet","corsa filhote", 10.000,"branco",2001)

c1.exibir()
c2.exibir()