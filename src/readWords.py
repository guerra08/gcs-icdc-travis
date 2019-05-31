import random
f = open("/home/18103819/gcs-icdc-travis/src/words/20words.txt","r")

palavras = []
for line in f:
    formatada = line.rstrip()
    palavras.append(formatada)
print(random.choice(palavras))