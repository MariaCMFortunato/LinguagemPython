#Os trimestre são do tipo inteiro de 1 até 4 - Não necessito defenir
MESES={1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}

print("")
trimestre = int(input("Digite o número do trimestre [1 a 4]: "))

if trimestre == 1:
    a = 'Os meses do primeiro trimestre são: %s, %s e %s' %(MESES.get(1), MESES.get(2), MESES.get(3))
    print(a)

elif trimestre == 2:
    b = 'Os meses do segundo trimestre são: %s, %s e %s' %(MESES.get(4), MESES.get(5), MESES.get(6))
    print(b)

elif trimestre == 3:
    c = 'Os meses do terceiro trimestre são: %s, %s e %s' %(MESES.get(7), MESES.get(8), MESES.get(9))
    print(c)

elif trimestre == 4:
    d = 'Os meses do quarto trimestre são: %s, %s e %s' %(MESES.get(10), MESES.get(11), MESES.get(12))
    print(d)

else:
    print("Erro o trimestre tem de ser entre 1 e 4!")



