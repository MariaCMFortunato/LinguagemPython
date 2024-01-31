#Classe de produtos de uma loja do tipo supermercado
class ProdutoSupermercado:
    # Os produtos caracterizam-se genericamente por um tipo, nome,e um código e iniciam-se sempre com sotck = 0
    #Trata-se de uma superclasse que será divida por tipo de produto

    def __init__(self, tipo, nome, codigo):
        self.tipo = tipo
        self.nome = nome
        self.codigo = codigo
        self.stock = 0

    #Insereção do stock inicial
    def stockInicial(self, quantidade):
        self.quantidade = quantidade
        self.stock = quantidade

    #Para reforçar o stock, compro uma certa quantidade
    def comprarProduto(self, quantidade):
        self.quantidade=quantidade
        self.stock += quantidade
        print(f"\nForam compradas {self.quantidade} unidades de {self.nome}. O stock é agora de {self.stock} unidades")

    #Quando vendo atualizo o stock, se o stock for suficiente se não não faz nada
    def venderProduto(self, quantidade):
        if self.stock >= quantidade:
            self.quantidade=quantidade
            self.stock -= quantidade
            print(f"\nForam vendidas {self.quantidade} unidades de {self.nome}. O stock é agora de {self.stock} unidades")
        else:
            print("\nStock insuficiente para vender essa quantidade!")


class Mercearia(ProdutoSupermercado):
    #Produtos do tipo mercearia de um supermercado
    #Classe filha de PrdoutoSupermercado
    def __init__(self, tipo, nome, codigo):
        super().__init__(tipo, nome, codigo)
        self.tipo="Mercearia"
        self.valido = True
    
    #Só se compra se o stock estiver for de 5 unidades ou menos
    def comprarProduto(self, quantidade):
        if self.stock <= 5:
            self.quantidade=quantidade
            self.stock += quantidade
            print(f"\nForam compradas {self.quantidade} unidades de {self.nome}. O stock é agora de {self.stock} unidades")
        else:
            print(f"\nAinda tem {self.stock} unidade em stock. Não foi efetuada compra!")
    #Alterar a validade do produto
    def alterarValidProdMercearia(self):
        if self.valido == True:
            self.valido = False
        elif self.valido ==False:
            self.valido = True

    #Destruir produto fora da validade
    def DestruirProdMercearia(self, quantidade):
        if self.stock >= quantidade:
            if self.valido == False:
                self.quantidade=quantidade
                self.stock -= quantidade
                print(f"\nForam destruidas {self.quantidade} unidades de {self.nome}. O stock é agora de {self.stock} unidades")
        else:
            print("\nErro! Stock insuficiente para destruir essa quantidade!")
    
def main():
    agua1 = ProdutoSupermercado("Agua Com Gás", "Frize Limão 0,75 cl", 123456789)
    arroz1 = Mercearia("Mercearia", "Arroz Agulha Europa 1kg",123456789)

    agua1.stockInicial(100)
    print(f"\nO sotck de {agua1.nome} e de {agua1.stock} unidades")

    arroz1.stockInicial(20)
    print(f"\nO sotck de {arroz1.nome} e de {arroz1.stock} unidades")

    agua1.comprarProduto(50)
    agua1.venderProduto(6)

    arroz1.comprarProduto(50)
    arroz1.venderProduto(5)
    arroz1.DestruirProdMercearia(15)

    print("")#cruiar linha em branco no fim da execução

main()