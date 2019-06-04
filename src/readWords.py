import random
f = open("./words/20words.txt","r")

def randomWord():
    palavras = []
    for line in f:
        formatada = line.rstrip()
        palavras.append(formatada)
    return random.choice(palavras)
