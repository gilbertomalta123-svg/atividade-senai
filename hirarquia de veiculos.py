class Veiculo:

    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max
        

    def mover(self):
        print(f"O veículo {self.marca} está se movendo!")

    def exibir(self):
        print(f"Marca: {self.marca}")
        print(f"Velocidade máxima: {self.velocidade_max} km/h")
        print(f"Litros de combustivel : {self.combustivel}L")

class Carro(Veiculo):
    def __init__(self, marca, velocidade_max,num_porta,combustivel):
        super().__init__(marca, velocidade_max)
        self.num_porta=num_porta
        self.combustivel=combustivel
    
    def exibir(self):
      super().exibir()
      print(f"\nNúmero de portas: {self.num_porta}")

c1=Carro("toyota",180,4,50)

c1.mover ()
c1.exibir()

class bike:
    def __init__(self,marca,velocidade_max):
       self.marca=marca
       self.velocidade_max=velocidade_max

    def mover(self):
        print(f"O veículo {self.marca} está se movendo!")

    def exibir (self):
       print(f"Marca: {self.marca}")
       print(f"Velocidade máxima: {self.velocidade_max} km/h")  

class Bicicleta(bike):
    def __init__(self, marca, velocidade_max,num_macha,pedalada):
        super().__init__(marca, velocidade_max)
        self.num_macha=num_macha
    

    def exibir(self):
        super().exibir()
        print(f"A BICICLETA TEM : {self.num_macha} MACHA")
    

b1=Bicicleta("Caloi",10,1,132)

b1.mover()
b1.exibir()

       
