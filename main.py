# main.py
import tkinter as tk
from tkinter import ttk

from geocode import geocode_single_city
from weather import get_weather_text
from news import get_news_text

def fetch_data():
    """
    Called when 'Get Data' button is pressed:
    1) Geocode city, fetch weather
    2) Fetch news for the country code
    3) Display both in their respective text widgets
    """
    city = city_entry.get().strip()
    country = country_entry.get().strip().lower()

    # --- Fetch Weather ---
    if city:
        lat, lon, resolved_name = geocode_single_city(city)
        if lat is not None and lon is not None:
            weather_info = get_weather_text(lat, lon, resolved_name)
        else:
            weather_info = f"Could not find valid coordinates for '{city}'."
    else:
        weather_info = "Please enter a city for weather."

    # Display weather text
    weather_text_area.config(state='normal')
    weather_text_area.delete('1.0', tk.END)
    weather_text_area.insert(tk.END, weather_info)
    weather_text_area.config(state='disabled')

    # --- Fetch News ---
    if country:
        news_info = get_news_text(country)
    else:
        news_info = "Please enter a 2-letter country code for news."

    # Display news text
    news_text_area.config(state='normal')
    news_text_area.delete('1.0', tk.END)
    news_text_area.insert(tk.END, news_info)
    news_text_area.config(state='disabled')


def main():
    root = tk.Tk()
    root.title("Weather & News app")

    main_frame = ttk.Frame(root, padding=10)
    main_frame.pack(fill='both', expand=True)

    # Input frame at the top
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(fill='x', pady=5)

    # City label
    city_label = ttk.Label(input_frame, text="Enter City:")
    city_label.pack(side='left', padx=5)

    # City entry
    global city_entry
    city_entry = ttk.Entry(input_frame, width=15)
    city_entry.pack(side='left')

    # Country code label
    country_label = ttk.Label(input_frame, text="Enter Country Code:")
    country_label.pack(side='left', padx=5)

    # Country entry
    global country_entry
    country_entry = ttk.Entry(input_frame, width=5)
    country_entry.pack(side='left')

    # Button
    get_data_button = ttk.Button(input_frame, text="Get Data", command=fetch_data)
    get_data_button.pack(side='left', padx=5)

    # Frames for weather/news
    weather_frame = ttk.LabelFrame(main_frame, text="Weather Forecast")
    news_frame = ttk.LabelFrame(main_frame, text="News Headlines")

    weather_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
    news_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)

    global weather_text_area, news_text_area
    weather_text_area = tk.Text(weather_frame, wrap='word', width=40, height=20, state='disabled')
    weather_text_area.pack(fill='both', expand=True)

    news_text_area = tk.Text(news_frame, wrap='word', width=40, height=20, state='disabled')
    news_text_area.pack(fill='both', expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
