def Imc(peso, altura):
    #função que calcula o IMC
    # recebe o peso e a altura e retorna o IMC
    imc =peso/(altura ** 2)
    return imc

def nivelImc(peso, altura):
    # verifica o nivel de IMC e retorna a classificação
    # recebe o cálculo efetuado pela função anterior
    imc=Imc(peso, altura)
    nivelImc= ""
    if imc < 18.5:
        nivelImc="Peso Corporal Baixo"
    elif imc < 25:
        nivelImc="Peso Normal"
    elif imc < 30:
        nivelImc="Excesso de Peso"
    elif imc < 35:
        nivelImc="Obesidade Grau I"
    elif imc < 40:
        nivelImc="Obesidade Grau II"
    else:
        nivelImc="Obesidade Mórbida"
    return nivelImc

if __name__ == '__main__':
    #pedido de informação ao utilizador e atribuição à variável peso
    peso=float(input("Indique o seu peso em Kg: "))
    #pedido de informação ao utilizador e atribuição à variável altura
    altura=float(input("Indique a sua altura em m: "))
    # atribuição à variável indice do resultado da função Imc
    indice=Imc(peso, altura)
    #atribuição à variável nível da classificação obtida na função nivelImc
    nivel=nivelImc(peso, altura)
    #criação da string com o resumo de informação introduzida pelo utilizador 
    #para imprimir mais tarde - método format
    resumo= "O seu peso é {:.2f} kg, a sua altura é {:.2f} m".format(peso, altura)
    #Criação da string com os resultados das funções, para imprimir mais tarde
    #- método format
    resultado="O seu IMC é {:.2f} a que corresponde a classificação {}".format(indice,nivel)
    #impressão das strings - - método format
    print("\n{}\n{}\n".format(resumo,resultado))
    #impressão das strings - - método f-string
    print(f"\n{resumo}\n{resultado}")
