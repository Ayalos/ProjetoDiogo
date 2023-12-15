class SensorPorta:
    def __init__(self, estado_inicial="fechada"):
        self.estado = estado_inicial
        self.on = "on"
        self.off = "off"
        self.luz = "luz"

    def abrir(self):
        self.estado = "aberta"
        self.luz = self.on

    def fechar(self):
        self.estado = "fechada"
        self.luz = self.off


    def verificar_estado(self):
        return self.estado

porta = SensorPorta()
