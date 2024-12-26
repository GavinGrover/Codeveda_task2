import requests #importing request module

api_key = '07f24fa43d5e15034ff0a0ad94ee418b'    #api key from OpenWeather

user_input = input("Enter City Name : ")    #user input for city 

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={'07f24fa43d5e15034ff0a0ad94ee418b'}"
)   #requesting web for providing weather and temperature of city provided by user

if weather_data.json().get('cod') == '404':
    print("No City Found")  #applying if conditions if city not found
    
else:    #if city found will display weather and temperature in degree celcius
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºC")