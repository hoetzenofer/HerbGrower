class Plant:
    def __init__(self, name: str, latin_name: str, temperature: float, humidity: float, moisture: float):
        self.name = name
        self.latin_name = latin_name
        self.temperature = temperature
        self.humidity = humidity
        self.moisture = moisture

    def request(self, change: function, priority: float):
        pass
