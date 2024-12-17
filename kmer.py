import sys

# Verifica se os argumentos necessários foram fornecidos
if len(sys.argv) < 3:
    print("Insira o ficheiro e o tamanho do kmer!")
    sys.exit(1)

# Lê o nome do arquivo e o tamanho do kmer
filename = sys.argv[1]
kmer = int(sys.argv[2])

print(f"Sequence name    Most frequent k-mer (k={kmer})    # of occurrences    Least frequent k-mer (k={kmer})    # of occurrences")
#sys.stdout.write(f"Sequence name    Most frequent k-mer (k={kmer})    # of occurrences    Least frequent k-mer (k={kmer})    # of occurrences\n")

#print("Sequence name    Most frequent k-mer (k=" + str(kmer) + ")   # of occurrences    Least frequent k-mer (k=" + str(kmer) + ")  # of occurrences")
#print(f"Sequence name    Most frequent k-mer (k=" + str(kmer) + ")   # of occurrences    Least frequent k-mer (k=" + str(kmer) + ")  # of occurrences")

with open(filename, "r") as file:
    sequence_header = file.readline()[:-1]  # Lê a primeira linha do arquivo sem a quebra de linha
    current_kmer = file.read(kmer)  # Lê os primeiros 'kmer' caracteres

    conta_kmers = {current_kmer: 1}  # Dicionário para contar a ocorrência de cada kmer

    while True:
        current_kmer = current_kmer[1:]  # Remove o primeiro caractere
        next_char = file.read(1)  # Lê o próximo caractere

        if next_char == "":  # Fim do arquivo
            maxfrequence = max(conta_kmers.values())
            minfrequence = min(conta_kmers.values())

            for key in conta_kmers:  # Encontra o kmer menos frequente
                if conta_kmers[key] == minfrequence:
                    least_frequent_kmer = key
                    break

            for key in conta_kmers:  # Encontra o kmer mais frequente
                if conta_kmers[key] == maxfrequence:
                    most_frequent_kmer = key
                    break

            #print(sequence_header.lstrip(">") + "    " + most_frequent_kmer + "    " + str(maxfrequence) + "    " + least_frequent_kmer + "    " + str(minfrequence))
            #print(sequence_header[1:]  + "    " + most_frequent_kmer + "    " + str(maxfrequence) + "    " + least_frequent_kmer + "    " + str(minfrequence))
            print(f"{sequence_header[1:]}    {most_frequent_kmer}    {maxfrequence}    {least_frequent_kmer}    {minfrequence}")            
            break

        if next_char == "\n":  # Ignora quebras de linha
            next_char = file.read(1)

        if next_char == ">":

            maxfrequence = max(conta_kmers.values())
            minfrequence = min(conta_kmers.values())

            for key in conta_kmers:  # Encontra o kmer menos frequente
                if conta_kmers[key] == minfrequence:
                    least_frequent_kmer = key
                    break

            for key in conta_kmers:  # Encontra o kmer mais frequente
                if conta_kmers[key] == maxfrequence:
                    most_frequent_kmer = key
                    break
            
            #print(sequence_header.lstrip(">") + "    " + most_frequent_kmer + "    " + str(maxfrequence) + "    " + least_frequent_kmer + "    " + str(minfrequence))
            #print(sequence_header[1:]  + "    " + most_frequent_kmer + "    " + str(maxfrequence) + "    " + least_frequent_kmer + "    " + str(minfrequence))
            print(f"{sequence_header[1:]}    {most_frequent_kmer}    {maxfrequence}    {least_frequent_kmer}    {minfrequence}")            

            sequence_header = file.readline()[:-1]
            sequence_header = next_char + sequence_header

            conta_kmers.clear()

            current_kmer = file.read(kmer)
            conta_kmers = {current_kmer: 1}

            continue


        current_kmer = current_kmer + next_char  # Atualiza o kmer

        if len(current_kmer) != kmer:  # Valida o tamanho do kmer
            continue

        if current_kmer in conta_kmers:  # Incrementa a contagem se já existir no dicionário
            conta_kmers[current_kmer] += 1
        else:
            conta_kmers[current_kmer] = 1  # Adiciona o kmer ao dicionário

    