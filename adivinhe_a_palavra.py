secreto = 'fotografia'
digitadas = []
chances = 10

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')


    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
     
    digitadas.append(letra)
    if letra in secreto:
        print(f'a letra "{letra}" existe na palavra secreta')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario = secreto_temporario + letra_secreta
        else:
            secreto_temporario = secreto_temporario + '*'
    
    if secreto_temporario == secreto:
        print('Parabéns!!! Você adivinhou a palavra secreta.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    
    if letra not in secreto:
        chances = chances - 1
    
    print(f'Você ainda tem {chances} chances.')
    print()

    
