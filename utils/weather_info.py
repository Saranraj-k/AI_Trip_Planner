import requests

class WeatherForecastTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
    
    def get_current_weather(self, place:str):
        """Get current weather of a place"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": place,
                "appid": self.api_key
            }
            reponse = requests.get(url, params=params)
            return reponse.json() if reponse.status_code == 200 else {}
        except Exception as e:
            raise e
        
    def get_forecast_weather(self, place:str):
        """Get weather forecast of a place"""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": place,
                "appid": self.api_key,
                "cnt":10,
                "units":"metric"
            }
            reponse = requests.get(url, params=params)
            return reponse.json() if reponse.status_code == 200 else {}
        except Exception as e:
            raise e