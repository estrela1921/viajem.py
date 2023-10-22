import csv

# Defina as perguntas e as opções de resposta
perguntas = [
    "1. Você gosta de viajar? (1 - Sim, 2 - Não, 3 - Não sei responder)",
    "2. Você já viajou para outro país? (1 - Sim, 2 - Não, 3 - Não sei responder)",
    "3. Você costuma viajar em família? (1 - Sim, 2 - Não, 3 - Não sei responder)",
    "4. Você se planeja para fazer uma viajem? (1 - Sim, 2 - Não, 3 - Não sei responder)"
]

# Nome do arquivo .csv para armazenar os dados
arquivo_csv = "dados_pesquisa.csv"
# Abra o arquivo .csv para escrita
with open(arquivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Idade", "Gênero", "Resposta_1", "Resposta_2", "Resposta_3", "Resposta_4", "Data e Hora"])

    while True:
        print("Bem vindo a nossa Pesquisa sobre viajem")
        idade = input("  Para começarmos nos Informe sua idade (ou digite '00' para encerrar): ")
        if idade == '00':
            break

        genero = input("Informe seu gênero: ")
        respostas = []

        for pergunta in perguntas:
            resposta = input(pergunta)
            respostas.append(resposta)

        # Registre a data e hora da resposta
        ''''writer.writerow([idade, genero] + respostas + [data_hora]'''
