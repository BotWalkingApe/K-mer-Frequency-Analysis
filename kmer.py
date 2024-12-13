import sys

# Verifica se os argumentos necessários foram fornecidos
if len(sys.argv) < 3:
    print("Insira o ficheiro e o tamanho do kmer!")
    sys.exit(1)

# Lê o nome do arquivo e o tamanho do kmer
filename = sys.argv[1]
kmer = int(sys.argv[2])

print("Sequence name    Most frequent k-mer (k=" + str(kmer) + ")   # of occurrences    Least frequent k-mer (k=" + str(kmer) + ")  # of occurrences")

with open(filename, "r") as file:
    line = file.readline()[:-1]  # Lê a primeira linha do arquivo sem a quebra de linha
    stop = file.read(kmer)  # Lê os primeiros 'kmer' caracteres

    conta_kmers = {stop: 1}  # Dicionário para contar a ocorrência de cada kmer

    while True:
        stop = stop[1:]  # Remove o primeiro caractere
        aux = file.read(1)  # Lê o próximo caractere

        if aux == "":  # Fim do arquivo
            maxfrequence = max(conta_kmers.values())
            minfrequence = min(conta_kmers.values())

            for key in conta_kmers:  # Encontra o kmer menos frequente
                if conta_kmers[key] == minfrequence:
                    keyless = key
                    break

            for key in conta_kmers:  # Encontra o kmer mais frequente
                if conta_kmers[key] == maxfrequence:
                    keymax2 = key
                    break

            print(line[1:]  + "    " + keymax2 + "    " + str(maxfrequence) + "    " + keyless + "    " + str(minfrequence))
            break

        if aux == "\n":  # Ignora quebras de linha
            aux = file.read(1)

        if aux == ">":

            maxfrequence = max(conta_kmers.values())
            minfrequence = min(conta_kmers.values())

            for key in conta_kmers:  # Encontra o kmer menos frequente
                if conta_kmers[key] == minfrequence:
                    keyless = key
                    break

            for key in conta_kmers:  # Encontra o kmer mais frequente
                if conta_kmers[key] == maxfrequence:
                    keymax2 = key
                    break
            
            print(line[1:]  + "    " + keymax2 + "    " + str(maxfrequence) + "    " + keyless + "    " + str(minfrequence))

            line = file.readline()[:-1]
            line = aux + line

            conta_kmers.clear()

            stop = file.read(kmer)
            conta_kmers = {stop: 1}

            continue


        stop = stop + aux  # Atualiza o kmer

        if len(stop) != kmer:  # Valida o tamanho do kmer
            continue

        if stop in conta_kmers:  # Incrementa a contagem se já existir no dicionário
            conta_kmers[stop] += 1
        else:
            conta_kmers[stop] = 1  # Adiciona o kmer ao dicionário

    