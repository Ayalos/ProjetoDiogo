class VentiladorCongelador:
    def __init__(self):
        self.ventilador = "off"
        self.temperatura = 0.0
        self.degelo = "off"

    def fazer_degelo(self):
        self.degelo = "on"
        print("Iniciando degelo")

    def ligar_ventilador(self, sensor):
        self.sensores = sensor
        self.temperatura = self.sensores.temperatura
        while self.temperatura <= -17.99:
            self.temperatura = self.sensores.updateTemperatura()
            self.ventilador = "on"
            print(self.temperatura)
            print("Ventilador ligado")
            if self.temperatura <= -22.99:
                self.fazer_degelo()

    def desligar_ventilador(self):
        self.ventilador = "off"
        print("Ventilador desligado")