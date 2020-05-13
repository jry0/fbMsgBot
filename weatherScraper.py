#inspired by https://www.thepythoncode.com/article/get-weather-data-python
from bs4 import BeautifulSoup as bs
import requests

def getWeatherData(region):

    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather+" + region

    session = requests.Session()
    session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    session.headers['Accept-Language'] = "en-US,en;q=0.5"
    session.headers['Content-Language'] = "en-US,en;q=0.5"
    html = session.get(URL)

    soup = bs(html.text, "html.parser")

    # result dictionary
    result = {} 
    # get region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # get current temp
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get current time
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get current weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get % humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # get wind condition
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
   
    # get future info
    futureInfo = []
    days = soup.find("div", attrs={"id": "wob_dp"}).findAll("div", attrs={"class": "wob_df"})
    for day in days:
        # get the name of the day
        day_name = day.find("div", attrs={"class": "vk_lgy"}).attrs['aria-label']
        # get weather status
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # max temp
        max_temp = temp[0].text
        # min temp
        min_temp = temp[2].text
        futureInfo.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['futureInfo'] = futureInfo
    return result
    