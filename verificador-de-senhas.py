#Código desenvolvido como desafio de código da DIO
def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False
    caracteres_especiais = "!@#$%^&*(),.?\:{}|<>"

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

    for char in senha:
        if char.isupper():
            tem_letra_maiuscula = True
        elif char.islower():
            tem_letra_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_caractere_especial = True

    # Verificando se todos os critérios são atendidos
    if not tem_letra_maiuscula:
        return "Sua senha nao atende aos requisitos de seguranca."
    if not tem_letra_minuscula:
        return "Sua senha nao atende aos requisitos de seguranca."
    if not tem_numero:
        return "Sua senha nao atende aos requisitos de seguranca."
    if not tem_caractere_especial:
        return "Sua senha nao atende aos requisitos de seguranca."

    # Verificando se a senha contém sequências comuns
    sequencias_comuns = ["123456", "abcdef"]
    for sequencia in sequencias_comuns:
        if sequencia in senha:
            return "Sua senha contém uma sequência comum. Tente uma senha mais complexa."

    # Verificando se a senha contém palavras comuns
    palavras_comuns = ["password", "123456", "qwerty"]
    if senha in palavras_comuns:
        return "Sua senha e muito comum. Tente uma senha mais complexa."

    return 'Sua senha atende aos requisitos de seguranca. Parabens!'

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)
