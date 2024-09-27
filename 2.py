def verificar_letra_a(string):
    # Contar a quantidade de 'a' e 'A'
    contagem = string.count('a') + string.count('A')
    
    # Verifica se a letra 'a' existe na string
    if contagem > 0:
        return True, contagem
    else:
        return False, contagem

# String previamente definida
string = "Hoje é um ótimo dia para aprender Python!"

# Verifica a existência da letra 'a' e a contagem
existe, quantidade = verificar_letra_a(string)

# Exibe o resultado
if existe:
    print(f"A letra 'a' ocorre {quantidade} vezes na string.")
else:
    print("A letra 'a' não está presente na string.")
