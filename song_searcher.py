import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
LOOKBACK_DATE = "2000-08-12"  #input("Which date do you want to travel to? Enter as YYYY-MM-DD: ")
CHART_URL = f"{BILLBOARD_URL}{LOOKBACK_DATE}/"

response = requests.get(CHART_URL)
song_website = response.text

soup = BeautifulSoup(song_website, "html.parser")
all_songs = soup.select(".o-chart-results-list__item h3.c-title")
songs = [song.getText().strip() for song in all_songs]
# print(songs)

