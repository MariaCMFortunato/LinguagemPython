import pandas
import sqlite3
import os
from time import sleep


# Classes da aplicação Consumos de Veículos:
class Veiculo:
    # Os veículos caracterizam-se genericamente por terem matrícula, marca,modelo, cilindrada e tipo de energia
    # Trata-se de uma super classe que será dividida por tipo de enrgia motriz
    # Classe não usada nesta fase do projeto - será usada numa das fases seguintes

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
    #Classe não usada nesta fase do projeto - será usada numa das fases seguintes
    def __init__(self, matricula, marca, modelo, cilindrada, energia):
        super().__init__(matricula, marca, modelo, cilindrada, energia)
        self.tipoDeEnergia = "Gasóleo"


class Abastecimento:
    #Classe não usada nesta fase do projeto - será usada numa das fases seguintes
    def __init__(self, data, valorPago, kmsAtuais):
        self.data = data
        self.valorPago = valorPago
        self.kmsAtuais = kmsAtuais


class AbastGasoleo(Abastecimento):
    # Classe filha da classe Abastecimento usada para os veículos que abastecem gasóleo
    #Classe não usada nesta fase do projeto - será usada numa das fases seguintes
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
    def ficheiroAImportar():
        # recebe a indicação do ficheiro a importar e do caminho absoluto concatena a informação
        # depois de mudar a barra e devolve o caminho completo do ficheiro para importação, sem
        # extensão do mesmo
        FICHEIRO = input(
            "\033[36mIndique o nome do ficheiro a importar: \033[m")
        CAMINHO = input(
            "\033[36mIndique o caminho do ficheiro a importar: \033[m")
        CAMINHO.replace('\\', '/')
        CaminhoCompleto = CAMINHO+"/"+FICHEIRO
        return CaminhoCompleto

    def colunasAImportar(consumos):
        # tendo em conta que pode não ser necessário importar todas as colunas do ficheiro
        # pede-se ao utilizador que indique as colunas a importar, parando o ciclo com uma
        # string vazia
        i = 0
        colunas = []
        print("")
        while True:
            coluna = input("\033[3;35mQual a coluna a importar: \033[m")
            if coluna != "":
                colunas.append(coluna)
            else:
                break
        # criar o subconjunto das colunas a importar
        consumoSubset = consumos[colunas]
        # ["data", "valor", "preço litro", "kms totais"]
        # retorna as primeiras 50 linhas
        consumoSubset.head(50)
        # retorna o subconjunto de dados criado
        return consumoSubset

    def importaCSV():
        # instância que armazena a informação do ficheiro e do caminho do ficheiro a importar
        caminho = ImportaDados.ficheiroAImportar()
        # instância que armazena os dados do ficheiro importado
        consumosf = pandas.read_csv(f"{caminho}.csv", sep=";")
        consumosf2 = ImportaDados.colunasAImportar(consumosf)
        df_dados = pandas.DataFrame(consumosf2)
        return df_dados
        # ImportaDados.imprimirDados(df_dados)
        # consumosf2.rename(columns={"Data":"data", "Total Pago":"valor", "Valor p/ Litro":"preço litro", "Litros":"litros", "Km Antes / Após do Abastecimento":"kms totais","Km Percorridos":"km percorridos","Media de Consumo por 100Km":"Consumo aos 100 kms" })

    def importaEXCEL():
        caminho = ImportaDados.ficheiroAImportar()
        consumosf = pandas.read_excel(f"{caminho}.xlsx")
        consumosf2 = ImportaDados.colunasAImportar(consumosf)
        df_dados = pandas.DataFrame(consumosf2)
        return df_dados
        # ImportaDados.imprimirDados(df_dados)
        # consumosf.rename(columns={"Data":"data", "Total Pago":"valor", "Valor p/ Litro":"preço litro", "Litros":"litros", "Km Antes / Após do Abastecimento":"kms totais","Km Percorridos":"km percorridos","Media de Consumo por 100Km":"Consumo aos 100 kms" })

    def imprimirDados(df_dados):
        # imprime os dado no ecrã
        print("")
        print(Menu.linha())
        print(df_dados)
        print(Menu.linha())
        os.system("pause")
        # sleep(3)


class ExportaDados:
    def dadosAExportar():
        BASEDADOS = input(
            "\033[36mIndique o nome da Base de Dados: \033[m")
        CAMINHO = input(
            "\033[36mIndique o caminho do ficheiro: \033[m")
        CAMINHO.replace('\\', '/')
        bDados = CAMINHO+"/"+BASEDADOS
        return bDados

    def menuBD():
        escolhas = [
            "Preciso de importar um fciheiro CSV",
            "Preciso de importar um fciheiro EXCEL",
            "Já importei os dados a exportar",
            "Menu Prinicipal"
        ]

        while True:
            os.system("cls")
            Menu.cabecalho("\033[33mDADOS A EXPORTAR\033[m")
            escolha = Menu.menu(escolhas)
            if escolha == 1:
                Menu.cabecalho("\033[33mIMPORTAR FICHEIRO CSV\033[m")
                df_dados = ImportaDados.importaCSV()
            elif escolha == 2:
                Menu.cabecalho("\033[33mIMPORTAR FICHEIRO EXCEL\033[m")
                df_dados = ImportaDados.importaEXCEL()
            elif escolha == 3:
                Menu.cabecalho("\033[33mEXPORTAR DADOS PARA TABELA SQL\033[m")
                ExportaDados.criarBD(df_dados)
            elif escolha == 4:
                Menu.cabecalho("\033[33mO PROGRAMA VAI TERMINAR!\033[m")
                break
            else:
                Menu.cabecalho("\033[31mERRO! Escolha uma opção válida!\033[m")
                os.system("pause")

    def criarBD(df_dados):
        baseDados = ExportaDados.dadosAExportar()
        conexao = sqlite3.connect(f"{baseDados}.db")
        df_dados.to_sql(name="consumos", con=conexao,
                        if_exists="replace", index=True, index_label="indice")
        print("\033[32mDados exportados comm sucesso!\033[m")
        os.system("pause")
        conexao.close


class ManipulaDados:
    def mostradados():
        baseDados = ExportaDados.dadosAExportar()
        conexao = sqlite3.connect(f"{baseDados}.db")
        cursor = conexao.cursor()
        matricula=input("\033[35mIndique a matrícula da viatura: \033[m")
    
        cursor.execute("SELECT kms FROM consumos WHERE matricula = ? ORDER BY data ASC LIMIT 1", (matricula,))
        kmsIniciais=cursor.fetchone()[0]

        cursor.execute("SELECT kms FROM consumos WHERE matricula = ? ORDER BY data DESC LIMIT 1", (matricula,))
        kmsFinais=cursor.fetchone()[0]

        kmsPercorridos = kmsFinais - kmsIniciais

        cursor.execute("SELECT SUM(valor/preco_litro) FROM consumos WHERE matricula = ? ", (matricula,))
        litros = cursor.fetchone()[0]

        consumo = (100 * litros) / kmsPercorridos
        consumoFormatado="{:.2f}".format(consumo)


        # cursor.execute("SELECT * FROM consumos WHERE matricula = ? ", (matricula,))
        # tabela = pandas.DataFrame(cursor.fetchall(), columns=[
        #                          "indice", "matricula", "data", "valor", "preco litro", "kms"])
        

        os.system("pause")
        #ImportaDados.imprimirDados(tabela)
        # print(f"\033[36mKms Iniciais da Viatura: {kmsIniciais}\033[m")
        # print(f"\033[36mKms Finais da Viatura: {kmsFinais}\033[m")
        # print(f"\033[36mKms percorridos pela Viatura: {kmsPercorridos}\033[m")
        # print(f"\033[36mLitros totais consumidos: {litros}\033[m")
        print("")
        Menu.cabecalho("\033[33mCONSUMO MÉDIO TOTAL DA VIATURA\033[m".format(matricula))
        print("\033[4;36m {:=^28} litros aos 100kms\033[m".format(consumoFormatado))
        print("")
        os.system("pause")

        conexao.close


class Menu:
    def linha(tamanho=50):
        return "\033[33m-\033[m" * tamanho

    def cabecalho(texto):
        print(Menu.linha())
        print(texto.center(50))
        print(Menu.linha())

    def menu(opcoes):
        contador = 1
        for item in opcoes:
            print(f"\033[33m{contador}\033[m - \033[34m{item}\033[m")
            contador += 1
        print(Menu.linha())
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
        os.system("cls")
        Menu.cabecalho("\033[33mMENU PRINCIPAL\033[m")
        escolha = Menu.menu(Menu.opcoes)
        if escolha == 1:
            Menu.cabecalho("\033[33mIMPORTAR FICHEIRO CSV\033[m")
            ImportaDados.importaCSV()
        elif escolha == 2:
            Menu.cabecalho("\033[33mIMPORTAR FICHEIRO EXCEL\033[m")
            ImportaDados.importaEXCEL()
        elif escolha == 3:
            Menu.cabecalho("\033[33mEXPORTAR DADOS PARA TABELA SQL\033[m")
            ExportaDados.menuBD()
        elif escolha == 4:
            Menu.cabecalho("\033[33mCALCULAR CONSUMO DE UM VEÍCULO\033[m")
            ManipulaDados.mostradados()
        elif escolha == 5:
            Menu.cabecalho("\033[33mO PROGRAMA VAI TERMINAR!\033[m")
            break
        else:
            Menu.cabecalho("\033[31mERRO! Escolha uma opção válida!\033[m")
            sleep(2)
