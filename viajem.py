 import csv
from datetime import datetime

class PesquisaViagem:
    def __init__(self, arquivo_csv):

        self.arquivo_csv = arquivo_csv
        
        self.perguntas = [
            "\n1. Você gosta de viajar? (1 - Sim, 2 - Não, 3 - Não sei responder)",

            "\n2. Você já viajou para outro país? (1 - Sim, 2 - Não, 3 - Não sei responder)",

            "\n3. Você costuma viajar em família? (1 - Sim, 2 - Não, 3 - Não sei responder)",

            "\n4. Você se planeja para fazer uma viagem? (1 - Sim, 2 - Não, 3 - Não sei responder)",

            "\n5. Quando você viaja você gosta de lugares com praia? (1 - Sim, 2 - Não, 3 - Não sei responder)",

            "\n6. Você gosta de viajar para lugares com cachoeira? ( 1 - Sim, 2 - Não, 3 - Não sei responder)"
        ]


    def realizar_pesquisa(self):
        # Abrindo o arquivo CSV para escrita
        with open(self.arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Idade", "Gênero"] + [f"Resposta_{i+1}" for i in range(len(self.perguntas))] + ["Data e Hora"])

            while True:
                print("\nBem-vindo à nossa Pesquisa sobre viagem")
                idade = input("\nPara começarmos, informe sua idade (ou digite '00' para encerrar): ")
                if idade == '00':
                    break            
    

                genero = input("\nInforme seu gênero: ")
                respostas = []

                for pergunta in self.perguntas:
                    resposta = input(pergunta)
                    respostas.append(resposta)
                    if not resposta in ["1","2","3"]: 
                        print("Resposta Inválida. Digite uma opção válida")   
                        resposta = input(pergunta)
                        
                             
                    data_hora = datetime.now().strftime("\n%d-%m-%y %H:%M:%S")
                writer.writerow([idade, genero] + respostas + [data_hora])

    def exibir_dados_pesquisa(self):
        # Abrindo o arquivo CSV para leitura
        with open(self.arquivo_csv, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            print("\nCabeçalho do CSV:")
            print(header)
            for row in reader:
                print("\nDados da pesquisa:")
                print("\nIdade:", row[0])
                print("\nGênero:", row[1])
                for i, pergunta in enumerate(self.perguntas):
                    print(pergunta, "\nResposta:", row[i + 2])
                print("\nData e Hora:", row[-1])
                print("\n")

if __name__ == "__main__":
    arquivo_csv = "dados_pesquisa.csv"
    pesquisa = PesquisaViagem(arquivo_csv)
    pesquisa.realizar_pesquisa()
    pesquisa.exibir_dados_pesquisa()


                

        
