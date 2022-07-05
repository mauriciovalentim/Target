#Definindo variaveis
numeroLimite = int(input("Digite um número: "))
numeroTotal = 0
primeiro = 0
segundo = 1
isFibonacci = False


#Fazendo calculo de fibonacci e descobrindo se o número faz parte
if numeroLimite == 0:
        isFibonacci = True

print(f"{primeiro}...{segundo}", end="...")
while numeroTotal <= numeroLimite:
    numeroTotal = primeiro + segundo
    primeiro = segundo
    segundo = numeroTotal
    print(f"{numeroTotal}", end="...")
    if numeroTotal == numeroLimite:
        isFibonacci = True

#imprimindo resultado
if isFibonacci:
    print(f"\n{numeroLimite} é um número da tabela de fibonacci")
else:
    print(f"\n{numeroLimite} não é um número da tabela de fibonacci")