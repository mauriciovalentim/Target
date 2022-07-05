palavra = str(input("Digite a palavra: "))
palavraNova = ""
for c in range(len(palavra), 0, -1):
    palavraNova += palavra[c-1]
print(palavraNova)
        

        