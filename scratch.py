import requests
from bs4 import BeautifulSoup

Youtube_trending_url = "https://www.youtube.com/feed/trending"

response = requests.get(Youtube_trending_url)

print("Status code", response.status_code)

#with open('trending.html', 'w') as f:
# f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')
print('page title', doc.title)

#Find all video divs
video_divs = doc.find_all('div', class_='ytd-video-renderer')

print(f'found {len(video_divs)} videos')

#beautiful contains no videos at this point on the initial page. so we have to simulate a headless browser that runs all the javascript on the page. Selenium comes into the picture. i.e. Selenium Automates browsers

#Moved from line 5 to scratch.py
