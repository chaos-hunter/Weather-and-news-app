# Weather-and-news-app
App was developed in python using tkinter as the UI it makes use of https://www.thenewsapi.com/ and https://open-meteo.com/ api 
How it works is you download the zip file unzip run in a python environment, run from main then it will bring up the app enter the city you want the weather for then the country code you want top3 news headlines for once you do click on Get data it will then show a weather forecast for the next 24 hours and top3 news headlines in that country
How the app works is when you request the city it send the city name to the geocoding api the geocoding then looks for the best match and returns the longitude and langitude which it gives to the weather api for it to get the weather of that city.
