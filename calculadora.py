def somar (a,b): return a + b
def subtrair (a,b): return a - b
def multiplicar (a,b): return a * b
def dividir (a,b):
    if b == 0 :return "ERRO!"
    return a/ b
def numeros (): 
        a = float (input("num 1 :"))
        b = float (input("num 2 :"))
        return a,b  
while True:

    op= input("operaçoes (+-*/) ou 0 para encerrar : )")
  
    if op == "0" :break

    if op =="+":
            a,b = numeros()
            print(f"resultado {somar(a,b)}")
    elif op =="-":
            a,b = numeros()
            print(f"resultado {subtrair(a,b)}")
    elif op == "*":
            a,b = numeros()
            print(f"resultado {multiplicar(a,b)}")
    elif op =="/":
                a,b = numeros()
                print(f"resultado {dividir(a,b)}")
    else:
            print("Erro!, digite um operador válido")
