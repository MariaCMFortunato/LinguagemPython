import pandas
import sqlite3
from time import sleep

# Classes da aplicação Consumos de Veículos:


class Veiculo:
    # Os veículos caracterizam-se genericamente por terem matrícula, marca,modelo, cilindrada e tipo de energia
    # Trata-se de uma super classe que será dividida por tipo de enrgia motriz

    def __init__(self, matricula, marca, modelo, cilindrada, energia):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.tipoDeEnergia = energia
        self.kms = 0

    # Insereção dos kms iniciais
    def kmsIniciais(self, kmsIniciais):
        self.kms = kmsIniciais

    def atualizarKms(self, kmsAtuais):
        self.kms = kmsAtuais


class VeiculoGasoleo(Veiculo):
    # Classe filha da classe Veículo, com tipo de energia prédefinido para gasóleo
    def __init__(self, matricula, marca, modelo, cilindrada, energia):
        super().__init__(matricula, marca, modelo, cilindrada, energia)
        self.tipoDeEnergia = "Gasóleo"


class Abastecimento:
    def __init__(self, data, valorPago, kmsAtuais):
        self.data = data
        self.valorPago = valorPago
        self.kmsAtuais = kmsAtuais


class AbastGasoleo(Abastecimento):
    # Classe filha da classe Abastecimento usada para os veículos que abastecem gasóleo
    def __init__(self, data, valorPago, precoLitro, kmsAtuais):
        super().__init__(data, valorPago, kmsAtuais)
        self.precoLitro = precoLitro

    # Quilometros percorridos entre abastecimentos
    def kmPercorridos(self, kmsAtuais):
        # Recebe os quilometros atuais
        self.kmsAtuais = kmsAtuais
        # Calcula os kms percorridos
        self.kmsPercorridos = Veiculo.kms - self.kmsAtuais
        # substitui o valor dos quilometros totais do veículo
        Veiculo.atualizarKms(kmsAtuais)

    def litrosAbastecidos(self, valorPago, precoLitro):
        # Recebe o valor pago no abastecimento
        self.valorPago = valorPago
        # Recebe o preço por litro
        self.precoLitro = precoLitro
        # Calcula o número de litros abastecidos
        self.litros = self.valorPago / self.precoLitro

    def consumoCemKms(self, kmsPercorridos, litros):
        # Recebe o valor calculado de kms percorridos
        self.kmsPercorridos = kmsPercorridos
        self.litros = litros
        self.consumo = (self.kmsPercorridos*100)/self.litros


class ImportaDados:
    # def __init__(self):
    #     pass

    def ficheiroAImportar():
        FICHEIRO = input(
            "\033[36mIndique o nome do ficheiro a importar: \033[m")
        CAMINHO = input(
            "\033[36mIndique o caminho do ficheiro a importar: \033[m")
        CAMINHO.replace('\\', '/')
        CaminhoCompleto = CAMINHO+"/"+FICHEIRO
        return CaminhoCompleto

    def colunasAImportar(consumos):
        i = 0
        colunas = []
        print("")
        while True:
            coluna = input("\033[3;35mQual a coluna a importar: \033[m")
            if coluna != "":
                colunas.append(coluna)
            else:
                break

        consumoSubset = consumos[colunas]
        # ["data", "valor", "preço litro", "kms totais"]
        consumoSubset.head(40)
        return consumoSubset

    def importaCSV():
        caminho = ImportaDados.ficheiroAImportar()
        consumosf2 = pandas.read_csv(f"{caminho}.csv", sep=";")
        consumosf2.head(40)
        consumosf3 = ImportaDados.colunasAImportar(consumosf2)
        df_dados = pandas.DataFrame(consumosf3)
        ImportaDados.imprimirDados(df_dados)
        # consumosf2.rename(columns={"Data":"data", "Total Pago":"valor", "Valor p/ Litro":"preço litro", "Litros":"litros", "Km Antes / Após do Abastecimento":"kms totais","Km Percorridos":"km percorridos","Media de Consumo por 100Km":"Consumo aos 100 kms" })

    def importaEXCEL():
        caminho = ImportaDados.ficheiroAImportar()
        consumosf = pandas.read_excel(f"{caminho}.xlsx")
        consumosf.head(40)
        consumosf3 = ImportaDados.colunasAImportar(consumosf)
        df_dados = pandas.DataFrame(consumosf3)
        ImportaDados.imprimirDados(df_dados)
        # consumosf.rename(columns={"Data":"data", "Total Pago":"valor", "Valor p/ Litro":"preço litro", "Litros":"litros", "Km Antes / Após do Abastecimento":"kms totais","Km Percorridos":"km percorridos","Media de Consumo por 100Km":"Consumo aos 100 kms" })

    def imprimirDados(df_dados):
        print("")
        print(linha())
        print(df_dados)
        print(linha())
        sleep(3)


def linha(tamanho=50):
    return "\033[33m-\033[m" * tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(50))
    print(linha())


def menu(opcoes):
    cabecalho("\033[33mMENU PRINCIPAL\033[m")
    contador = 1
    for item in opcoes:
        print(f"\033[33m{contador}\033[m - \033[34m{item}\033[m")
        contador += 1
    print(linha())
    opcao = int(input("\033[32mDigite a sua opção: \033[m"))
    return opcao


opcoes = [
    "Importar ficheiro CSV com dados da viatura",
    "Importar ficheiro EXCEL com dados da viatura",
    "Exportar dados para SQLite3",
    "Calculo do consumo de um veículo aos 100 kms",
    "Sair do programa"
]


if __name__ == '__main__':

    while True:
        escolha = menu(opcoes)
        if escolha == 1:
            cabecalho("\033[33mIMPORTAR FICHEIRO CSV\033[m")
            ImportaDados.importaCSV()
        elif escolha == 2:
            cabecalho("\033[33mIMPORTAR FICHEIRO EXCEL\033[m")
            ImportaDados.importaEXCEL()
        elif escolha == 3:
            cabecalho("\033[33mEXPORTAR DADOS PARA TABELA SQL\033[m")
        elif escolha == 4:
            cabecalho("\033[33mCALCULAR CONSUMO DE UM VEÍCULO\033[m")
        elif escolha == 5:
            cabecalho("\033[33mO PROGRAMA VAI TERMINAR!\033[m")
            break
        else:
            cabecalho("\033[31mERRO! Escolha uma opção válida!\033[m")
            sleep(2)
