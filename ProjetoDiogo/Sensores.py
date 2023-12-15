import requests


class Sensores():
    def __init__(self):
        self.data = self.getTemperaturaAmbiente()
        self.temperatura = 0
        self.k = 0.1
        self.Tm = self.data['temp_c']
        self.T0 = self.Tm + 5

    def updateTemperatura(self):
        self.temperatura += (-self.k * (self.T0 - self.Tm)) * 0.1
        return self.temperatura

    def getTemperatura(self):
        return self.temperatura

    def getTemperaturaAmbiente(self):
        result = requests.get(
            'https://api.weatherapi.com/v1/current.json',
            params={'q': '-8.64505,-35.575563', 'lang': 'Portuguese', 'key': '15f201a808464cd7b5a233328231312'},
            headers={'Accept': 'application/json'}, ).json()
        self.data = result['current']
        return self.data
