class Livros:
    def __init__(self,titulo,autor,pagina,disponivel):
       self.titulo=titulo
       self.autor=autor
       self.pagina=pagina
       self.disponivel=disponivel
    def Descriçao(self):
        print("TITULO",self.titulo)
        print("AUTOR",self.autor)
        print("PAGINAS",self.pagina)
        print("DISPONIVEL",self.disponivel)
    def Empresta(self):
        if self.disponivel == True:
            print("este livro pode ser emprestado ")
        else:
            print(" este livro ja esta emprestado ")
    def Devolvido(self):
        if self.disponivel == True:
            print(" este livro esta disponivel para emprestar")
        else:
            print("este livro nao foi devolvido")
            


lv1=Livros("Clean mode","Robert martin", 431 ,True)

lv2=Livros("Turma da monica","Machado De Acis",240,False)

x1=input("\ndeseja ver a situaçao do livro 1?")
lv1.Empresta()
x1=input("\ndeseja ver a descriçao do livro?")
lv1.Descriçao()
x1=input("ja devolveu entao?")
lv1.Devolvido()

x1=input("\ndeseja ver a situaçao do livro 2?")
lv2.Empresta()
x1=input("\ndeseja ver a descrição do livro 2?")
lv2.Descriçao()
x1=input("ja devolveu entao?")
lv2.Devolvido()