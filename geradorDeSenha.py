import random

# Definir caracteres permitidos
caracteres = '0123456789'

# Definir o tamanho da senha
tamanho = 6

# Gerar senha aleatória
senha = ''
for i in range(tamanho):
    senha += random.choice(caracteres)

# Imprimir senha gerada
print('Sua senha gerada é:', senha)
