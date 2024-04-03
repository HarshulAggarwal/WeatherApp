import streamlit as st
import requests

def get_weather(city):
    api_key = "4e5573ffc23c0ec3db5458a4b7fc8b9b"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def main():
    st.title("Weather App")

    city = st.text_input("Enter city name:", "")
    if st.button("Get Weather"):
        if city:
            weather_data = get_weather(city)
            if weather_data['cod'] == 200:
                st.success("Weather data retrieved successfully!")
                st.subheader(f"Current weather in {city}:")
                st.write("Description:", weather_data['weather'][0]['description'])
                st.write("Temperature:", weather_data['main']['temp'], "°C")
                st.write("Feels like:", weather_data['main']['feels_like'], "°C")
                st.write("Humidity:", weather_data['main']['humidity'], "%")
                st.write("Wind speed:", weather_data['wind']['speed'], "m/s")
                # Display weather icon
                icon_code = weather_data['weather'][0]['icon']
                icon_url = f"http://openweathermap.org/img/w/{icon_code}.png"
                st.image(icon_url, caption='Weather Icon', use_column_width=True)
            else:
                st.error("City not found. Please check the spelling or try another city.")
        else:
            st.warning("Please enter a city name.")

if __name__ == "__main__":
    main()
