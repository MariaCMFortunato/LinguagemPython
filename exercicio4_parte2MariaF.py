#definição da função trim_meses
def trim_meses(trim):
    #variável local contendo um dicionário de meses
    MESES={1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}

    #Variável local que conterá os meses do trimestre
    trimestre=[]

    #ciclo condicional em função do número do trimestre recebido em argumento
    if trim==1:
        #Ciclo que itera o dicionario de meses retirando os meses que correspondem ao trimestre
        for nr, mes in MESES.items():
            if nr <= 3:
                trimestre.append(mes)

    elif trim==2:
        for nr, mes in MESES.items():
            if nr >3 and nr <= 6:
                trimestre.append(mes)

    elif trim==3:
        for nr, mes in MESES.items():
            if nr >6 and nr <= 9:
                trimestre.append(mes)

    elif trim==4:
        for nr, mes in MESES.items():
            if nr >9 and nr <= 12:
                trimestre.append(mes)

    if trim > 0 and trim < 5:
        #output da informação armazenada nas 3 posições da variável trimestre
        print(f"%s, %s, %s" %(trimestre[0], trimestre[1], trimestre[2]))
    else:
        print("Erro! Trimestre inválido!")

#definição mda função main
def main():
    print("")#criar uma linha vazia
    trimestre = int(input("Digite o número do trimestre [1 a 4]: ")) #pedir a entrada com o nbúmero do trimestre
    trim_meses(trimestre) #chamar a função trim_meses

#inicio do programa
main()