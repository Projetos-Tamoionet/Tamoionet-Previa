import cv2
import numpy as np

class ReconhecedorImagem:

    def __init__(self, folhaCaderno, marcacao, resultado):
        self.folhaCaderno = folhaCaderno
        self.marcacao = marcacao
        self.resultado = resultado

    def identificarMarcacoes(self):
        metodo = cv2.TM_SQDIFF_NORMED

        folhaCaderno = cv2.imread(self.folhaCaderno)
        folhaCadernoEscalaCinza = cv2.cvtColor(folhaCaderno, cv2.COLOR_BGR2GRAY)
        marcacao = cv2.imread(self.marcacao, 0)
        larguraMarcacao, alturaMarcacao = marcacao.shape[::-1]

        resultadoCorrespondencia = cv2.matchTemplate(folhaCadernoEscalaCinza, marcacao, cv2.TM_CCOEFF_NORMED)
        threshold = .8

        correspondencias = np.where(resultadoCorrespondencia >= threshold)

        self.marcarRetanguloCorrespondencia(larguraMarcacao, alturaMarcacao, folhaCaderno, correspondencias)

        correspondencias = self.atualizarCorrespondencias(correspondencias, larguraMarcacao, alturaMarcacao)

        self.marcarAreaRecortar(folhaCaderno, correspondencias)

        self.recortarAreaMarcada(folhaCaderno, correspondencias)

    def marcarRetanguloCorrespondencia(self, larguraMarcacao, alturaMarcacao, folhaCaderno, correspondencias):
        for correspondencia in zip(*correspondencias[::-1]):
            cv2.rectangle(folhaCaderno, correspondencia, (correspondencia[0] + larguraMarcacao, correspondencia[1] + alturaMarcacao), (0, 0, 255), 2)

        cv2.imwrite(self.resultado + '/resultadoRetangulo.png', folhaCaderno)

    def atualizarCorrespondencias(self, correspondencias, larguraMarcacao, alturaMarcacao):
        correspondencias[0][0] += alturaMarcacao
        correspondencias[0][1] += alturaMarcacao
        correspondencias[1][1] += larguraMarcacao
        correspondencias[1][3] += larguraMarcacao

        return correspondencias

    def marcarAreaRecortar(self, folhaCaderno, correspondencias):
        cv2.line(folhaCaderno, (correspondencias[1][0], correspondencias[0][0]), (correspondencias[1][2], correspondencias[0][2]), (0, 0, 255), 2)
        cv2.line(folhaCaderno, (correspondencias[1][2], correspondencias[0][2]), (correspondencias[1][3], correspondencias[0][3]), (0, 0, 255), 2)
        cv2.line(folhaCaderno, (correspondencias[1][3], correspondencias[0][3]), (correspondencias[1][1], correspondencias[0][1]), (0, 0, 255), 2)
        cv2.line(folhaCaderno, (correspondencias[1][1], correspondencias[0][1]), (correspondencias[1][0], correspondencias[0][0]), (0, 0, 255), 2)

        cv2.imwrite(self.resultado + '/resultadoArea.png', folhaCaderno)

    def recortarAreaMarcada(self, folhaCaderno, correspondencias):
        xMin = min(correspondencias[1][0], correspondencias[1][1])
        xMax = max(correspondencias[1][2], correspondencias[1][3])
        yMin = min(correspondencias[0][0], correspondencias[0][1])
        yMax = max(correspondencias[0][2], correspondencias[0][3])

        cv2.imwrite(self.resultado + '/resultadoCortado.png', folhaCaderno[yMin:yMax, xMin:xMax])