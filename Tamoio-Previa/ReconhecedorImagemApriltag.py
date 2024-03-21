import cv2
import numpy as np
import os

class ReconhecedorImagemApriltag:

    def __init__(self, folhaCaderno, marcacao1, marcacao2, marcacao3, marcacao4, resultado):
        self.processarImagem(folhaCaderno, marcacao1, marcacao2, marcacao3, marcacao4, resultado)

    def processarImagem(self, caminhoFolhaCaderno,caminhoMarcacao1, caminhoMarcacao2, caminhoMarcacao3, caminhoMarcacao4, salvarEm):
        # Carrega as imagem
        folhaCaderno = cv2.imread(caminhoFolhaCaderno)

        # Converte para escala de cinza
        folhaCadernoEscalaCinza = cv2.cvtColor(folhaCaderno, cv2.COLOR_BGR2GRAY)

        # Atribui as marcações para um array
        marcacoes = [cv2.imread(caminhoMarcacao1), cv2.imread(caminhoMarcacao2), cv2.imread(caminhoMarcacao3), cv2.imread(caminhoMarcacao4)]

        # Cria array de correspondencias
        correspondencias = []

        # Define a faixa de redimensionamento da marcação
        faixaRedimensionamentos = np.linspace(0.1, 1.0, 50)

        for marcacao in marcacoes:
            # Converte a marcacao para a escala de cinza
            marcacaoEscalaCinza = cv2.cvtColor(marcacao, cv2.COLOR_BGR2GRAY)

            # Declara as variaveis de melhor correspondencia
            melhorCorrespondencia = None
            melhorScore = -np.inf

            # Percorre os redimensionamentos definidos
            for redimensionamento in faixaRedimensionamentos:
                # Redimensiona a marcação
                marcacaoEscalaCinzaRedimensionada = cv2.resize(marcacaoEscalaCinza, None, fx=redimensionamento, fy=redimensionamento)

                # Executa o método de correspondência
                resultado = cv2.matchTemplate(folhaCadernoEscalaCinza, marcacaoEscalaCinzaRedimensionada, cv2.TM_CCOEFF_NORMED)

                # Atribui os valores e a localização da correspondência
                minValor, maxValor, minLocalizacao, maxLocalizacao = cv2.minMaxLoc(resultado)

                # Se o valor máximo for maior que a pontuação atual, atribui ele
                if maxValor > melhorScore:
                    melhorCorrespondencia = (maxLocalizacao, marcacaoEscalaCinzaRedimensionada.shape[::-1])
                    melhorScore = maxValor

            # Adiciona a melhor correspondência no array de correspondências
            correspondencias.append(melhorCorrespondencia)

            # Desenhar o retângulo em torno da melhor correspondência
            #top_left = melhorCorrespondencia[0]
            #bottom_right = (top_left[0] + melhorCorrespondencia[1][0], top_left[1] + melhorCorrespondencia[1][1])
            #cv2.rectangle(folhaCaderno, top_left, bottom_right, (0, 0, 255), 2)

        # Exibe e salva a correspondência encontrada
        #cv2.imwrite(salvarEm + '/resultado_' + os.path.basename(caminhoFolhaCaderno), folhaCaderno)

        # Chama a função para delimitar a área de recorte
        self.marcarAreaRecortar(correspondencias, caminhoFolhaCaderno, folhaCaderno, salvarEm)

    def marcarAreaRecortar(self, correspondencias, caminhoFolhaCaderno, folhaCaderno, salvarEm):
        cv2.line(folhaCaderno,
                 (correspondencias[0][0][0] + correspondencias[0][1][0], correspondencias[0][0][1] + correspondencias[0][1][1]),
                 (correspondencias[2][0][0] + correspondencias[2][1][0], correspondencias[2][0][1]),
                 (0, 0, 255),
                 2)
        cv2.line(folhaCaderno,
                 (correspondencias[0][0][0] + correspondencias[0][1][0], correspondencias[0][0][1] + correspondencias[0][1][1]),
                 (correspondencias[1][0][0], correspondencias[1][0][1] + correspondencias[1][1][1]),
                 (0, 0, 255),
                 2)
        cv2.line(folhaCaderno,
                 (correspondencias[3][0][0], correspondencias[3][0][1]),
                 (correspondencias[2][0][0] + correspondencias[2][1][0], correspondencias[2][0][1]),
                 (0, 0, 255),
                 2)
        cv2.line(folhaCaderno,
                 (correspondencias[3][0][0], correspondencias[3][0][1]),
                 (correspondencias[1][0][0], correspondencias[1][0][1] + correspondencias[1][1][1]),
                 (0, 0, 255),
                 2)

        cv2.imwrite(salvarEm + '/resultado_' + os.path.basename(caminhoFolhaCaderno), folhaCaderno)