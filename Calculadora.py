expressao = ['*','+','-','/']
while True:
    
    bandeira = None
    
    try:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        conta = str(input('Digite a operação (*,+,-,/)'))
        bandeira = True
    except:
        bandeira = None 
        
    if bandeira == None:
        print('O resultado é inválido')
        continue
    
    if conta not in expressao:
        print('Essa expressao não é válida, tente novamente')
        continue
    
    if bandeira == True:
        if conta == '*':
            result=num1*num2
            print(f'O resultado de multiplicação é: {result}')
        elif conta == '-':
            result = num1 - num2
            print(f'O resultado da subtração é {result}')
        elif conta == '/':
            result = num1 / num2
            print(f'O resultado da divisão é {result}')
        elif conta == '+':
            result = num1 + num2
            print(f'O resultado da soma é {result}')
        else:
            print('Dessa forma está errada')
            continue

    sair = input('Quer sair do loop? Digite [sim] se não digite [não] : ').lower()
    
    if sair == 'sim':
        break
    elif sair == 'não':
        continue
    else:
        print('Não consegui entender, continue a calcular')