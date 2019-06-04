from readWords import randomWord

if __name__ == "__main__":
    erros = 0
    palavra = ""
    word = randomWord()
    n = len(word)

    for i in range(n):
        palavra += "_"

    print(palavra)

    while(erros < 5):
        x = input("Digite uma letra ou palavra caso queira chutar\n")

        if len(x) > 1:
            if x == word:
                print("Voce Acertou! Parabens :D")
                break
            else:
                print("Errou!")
                erros += 1

        if x in word:
           for i, character in enumerate(word):
               if x == character:
                   palavra = palavra[:i] + x + palavra[i+1:]
        else:
            print("Letra nao encontrada")
            erros += 1
        print("Palavra: " , palavra, "\nerros: ", erros)
