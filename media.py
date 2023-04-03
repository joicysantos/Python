# UNIVERSIDADE FEDERAL DE CAMPINA GRANDE
# JOICY DOS SANTOS SILVA
# CODIGO REPRESENTA UM PROGRAMA SIMPLES QUE CALCULA A MEDIA DA SOMA DE TRES NOTAS.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
notas = "Para as notas {}, {} e {}, sua média ficou: {}".format(nota1, nota2, nota3, media)

print(notas)