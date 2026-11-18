def celsius_para_faherenheit (c):
    return(c *9/5)+32

def km_para_minhas(km):
    return km * 0.621371

def kg_para_libras(kg):
    return kg * 2.20462

def area_retangular(largura:float,comprimento:float)->float:
  if largura <=0 or comprimento <=0:
     raise ValueError (" LARGURA OU COMPRIMENTO DEVEM SER MAIOR QUE 0 !")
  return largura * comprimento

def eh_primo(num):
   
    if num <= 1:
        return False
    

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Encontrou um divisor, logo não é primo
            
    return True



while True:
 print(" 1 - celsius_para_faherenheit ")
 print(" 2 - km_para_minhas")
 print(" 3 - kg_para_libra ")
 print(" 4 - calcular_area_retangulo")
 print(" 5 - maior_de_tres ")
 print(" 6 - eh_primo ")

 opcao =int(input("\nESCOLHA UMA DAS OPÇÔES :"))
 if opcao== 0 :break

 while opcao == 1:
    celsius=float(input("\nDIGITE PARA A CONVERSÃO :"))
    faherenheit=celsius_para_faherenheit(celsius)
    print("")
    print(f"\n  A TEMPERATURA EM faherenheit É {faherenheit} ")
    resp=input("\nDESEJA CONTINUAR NESSE PROGRAMA DE CONVERSÃO DE celsius_para_faherenheit (c) s/n :")
    if resp== "s":
       continue
    else:
       break
 while opcao== 2:
    km=float(input("\nDIGITE O KM PECORRIDO : "))
    milhas=km_para_minhas(km)
    print("")
    print(f"\n AS MILHAS PECORRIDA PELO KM E DE : {milhas}")
    resp=input("\nDESEJA CONTINUAR NESSE PROGRAMA DE CONVERSÃO DE celsius_para_faherenheit (c) s/n : ")
    if resp== "s":
        continue
    else:
        break
 while opcao== 3:
    kg=float(input("\nDIGITE OS KILOS PARA CONVERTE PARA LIBRAS :"))
    libras=kg_para_libras(kg)
    print(f"\nA CONVERSÃO DE KILOS PARA LIBRAS É : {libras}")
    resp=input("\nDESEJA CONTINUAR NESSE PROGRAMA DE CONVERSÃO DE celsius_para_faherenheit (c) s/n :")
    if resp== "s":
        continue
    else:
        break
 while opcao == 4 :
  valor= float(input("\n DIGITE O VALOR PARA CALCULAR :"))
  valor2= float(input("\n DIGITE O VALOR PARA CALCULAR :"))
  total=valor*valor2
  print(f"O VALOR DA AREA DO RETANGULO E :{total}")
  resp=input("\nDESEJA CONTINUAR NESSE PROGRAMA DE CONVERSÃO DE celsius_para_faherenheit (c) s/n : ")
  if resp== "s":
        continue
  else:
     break
 while opcao == 5:
    n1=float(input("\n DIGITE ALGUM NUMERO :"))
    n2=float(input("\n DIGITE ALGUM NUMERO :"))
    n3=float(input("\n DIGITE ALGUM NUMERO :"))

    if n1 >= n2 and n1 >= n3:
       print(f"n MAIOR NUMERO E {n1} ")
    elif n2>=n1 and n2 >= n3:
     print(f"\n MAIOR NUMERO E {n2} ")
    else:
       print(f"\nMAIOR NUMERO E {n3} ")
       resp=input("\nDESEJA CONTINUAR NESSE PROGRAMA DE CONVERSÃO DE celsius_para_faherenheit (c) s/n : ")
    if resp== "s":
        continue
    else:
        break
 while opcao==6:
  n1=int(input("DIGITE O NUMERO INTEIRO"))
  if eh_primo(n1):
    print(f"\n o numero {n1} E PRIMO")
  else:
   print(f"\no numero{n1} NAO E NUMERO PRIMO")
   resp=input("\nDESEJA CONTINUAR NESSE PROGRAMA DE CONVERSÃO DE celsius_para_faherenheit (c) s/n : ")
   if resp== "s":
    continue
   else:
     break

