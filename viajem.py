import csv
from datetime import datetime

class Perguntas:
    def __init__(self):
        self.perguntas = [
            "\n1. Você gosta de viajar? \n(1) Sim \n(2) Não \n(3) Não sei responder \n DIGITE: ",
            "\n2. Você já viajou para outro país? \n(1) Sim \n(2) Não \n(3) Não sei responder \n DIGITE: ",
            "\n3. Você costuma viajar em família? \n(1) Sim \n(2) Não \n(3) Não sei responder \n DIGITE: ",
            "\n4. Você se planeja para fazer uma viagem? \n(1) Sim \n(2) Não \n(3) Não sei responder \n DIGITE: ",
            "\n5. Quando você viaja você gosta de lugares com praia? \n(1) Sim \n(2) Não \n(3) Não sei responder \n DIGITE:  ",
            "\n6. Você gosta de viajar para lugares com cachoeira? \n(1) Sim \n(2) Não \n(3) Não sei responder \n DIGITE: "
        ]

class PesquisaViagem:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.perguntas = Perguntas().perguntas

    def realizar_pesquisa(self):
        with open(self.arquivo_csv, mode='a', newline='') as file:  # Abre o arquivo em modo de anexação ('a')
            writer = csv.writer(file)
            # Se o arquivo estiver vazio, escreve o cabeçalho
            if file.tell() == 0:
                writer.writerow(["Idade", "Gênero"] + [f"Resposta_{i+1}" for i in range(len(self.perguntas))] + ["Data", "Hora"])

            while True:
                print("\nBem-vindo à nossa Pesquisa sobre viagem pra começarmos Digite: \n(1)Feminino\n(2)Masculino\n(3)Não sei\n Logo em seguida digite:\n(1)Sim\n(2)Não\n(3)Não sei\n")
                idade = input("\nPara começarmos, informe sua idade (ou digite '00' para encerrar): ")
                if idade == '00':
                    break

                while True:
                    genero = input("(1) Feminino\n(2) Masculino\n(3) Não sei\n Informe seu gênero: " )
                    if genero in ["1", "2", "3"]:
                        break
                    else:
                        print("Gênero inválido. Digite uma opção válida (1, 2 ou 3)")

                respostas = []

                for pergunta in self.perguntas:
                    while True:
                        resposta = input(pergunta)
                        if resposta in ["1", "2", "3"]:
                            break
                        else:
                            print("Resposta Inválida. Digite uma opção válida (1, 2 ou 3)")

                    data_hora = datetime.now()
                    data = data_hora.strftime("%d-%m-%Y")
                    hora = data_hora.strftime("%H:%M:%S")
                    respostas.append(resposta)

                writer.writerow([idade, genero] + respostas + [data, hora])

    def exibir_dados_pesquisa(self):
        with open(self.arquivo_csv, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            print(header)
            for row in reader:
                print("\nDados da pesquisa:")
                print("\nIdade:", row[0])
                print("\nGênero:", row[1])
                for i, pergunta in enumerate(self.perguntas):
                    print(pergunta, "\nResposta:", row[i + 2])
                data = row[-2]  # Índice da coluna de data
                hora = row[-1]  # Índice da coluna de hora
                print("\nData:", data)
                print("Hora:", hora)

if __name__ == "__main__":
    arquivo_csv = "dados_pesquisa.csv"
    pesquisa = PesquisaViagem(arquivo_csv)
    pesquisa.realizar_pesquisa()
    pesquisa.exibir_dados_pesquisa()

    print("Obrigado por Participar de nossa pesquisa!")
