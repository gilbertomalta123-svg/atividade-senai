while True:
    print("")
    print("                     1-  PAR OU ÍMPAR                 ")
    print("                     2-  MULTIPLO DE 3                ")
    print("                     3-  MEDIA DE NOTA                ")
    print("")
    
    escolha = int(input("\nESCOLHA UMA DAS OPÇÕES :"))

    while escolha == 1:
        numero = int(input("\n INFORME O SEU NÚMERO :"))
        if numero % 2 ==0:
            print(f"\nO número digitado {numero} é par. ")
        else:
            print(f"\nO número digitado {numero} é ímpar")
        resp = input("\ndeseja continuar (s/n): ")
        if resp =="s":
                continue
        else:
                
                break
    while escolha == 2 :
         num = 3 
         for i in range (1,51):
              print (f"\n{i} e multiplo de {num}")
         resp = input("\ndeseja continuar (s/n): ")
         if resp =="s":
            continue
         else:
          break

    while escolha == 3 :

        nota1=float(input("\n digite a primeira do aluno : "))
        nota2=float(input("\n digite a segunda do aluno : "))
        nota3=float(input("\n digite a terceira do aluno : "))
        nota4=float(input("\n digite a quarta  do aluno : "))

        media = ( nota1 + nota2 + nota3 + nota4 ) /4
        result = media

        if media >7.0:
            print(f"\naluno aprovado com a media {result} ")
        else:
            print (f"\n reprovado com a media {result}")
            
         
         
