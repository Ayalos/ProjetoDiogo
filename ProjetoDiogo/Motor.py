import time
from VentiladorCongelador import VentiladorCongelador
from Sensores import Sensores


class Motor:

    def __init__(self):
        self.motorGeladeira = True
        self.motorCongelador = True
        self.temperatura = 0.0
        self.sensores = Sensores()  # Supondo que Sensores seja uma classe existente
        self.ventilador = VentiladorCongelador()


    def offGeladeira(self):
        self.motorGeladeira = False

    def offCongelador(self):
        self.motorCongelador = False
        self.ventilador.ligar_ventilador(self.sensores)

    def on(self):
        self.temperatura = self.sensores.updateTemperatura()
        while self.temperatura > -18:
            self.temperatura = self.sensores.updateTemperatura()

            print("Baixando a temperatura ", self.temperatura)
            if self.temperatura <= -18.00:
                print("Motor congelador desligada")
                self.offCongelador()
            elif self.temperatura <= 2.99 and self.temperatura >=2.00 :
                print("Motor geladeira desligado")
                self.offGeladeira()

###    def onCongelador():
###         self.temperatura = Sensores.updateTemperatura(self,1,false)
###         while temperatura > -18:
###             time.sleep(1)
###             temperatura = Sensores.updateTemperatura(self,1,false)
###         offCongelador()
        