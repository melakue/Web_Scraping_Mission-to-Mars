from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup 
import time
import pandas as pd
import os
import requests
import re
from splinter import Browser

#executable_path = {"executable_path":r"C:\Users\mewub408\PythonProject\GWARL201902DATA3-1\01-Lesson-Plans\12-Web-Scraping-and-Document-Databases\2\Activities\03-Ins_Craigslist\Solved\chromedriver.exe"}


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    #executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
     executable_path = {"executable_path":r"C:\Users\mewub408\PythonProject\GWARL201902DATA3-1\01-Lesson-Plans\12-Web-Scraping-and-Document-Databases\2\Activities\03-Ins_Craigslist\Solved\chromedriver.exe"}
     return Browser("chrome", **executable_path, headless=False)
#browser=Browser("chrome", **executable_path, headless=False)

def scrape():

    browser = init_browser()
    mars_info = {}

    url = "https://mars.nasa.gov/news"
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")

    mars_info["News_tile"]=news_soup.find('div', class_= "content_title").get_text()
    mars_info["Latest_p"] = news_soup.find('div', class_= "image_and_description_container").get_text()


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    soup_image = BeautifulSoup(html, "html.parser")

    featured_image_url = soup_image.find('article', class_='carousel_item').get('style')
    start = featured_image_url.find("url('")
    end = featured_image_url.find("');")
    featured_image_url= featured_image_url[start+len("url('"):end]
    featured_image_url=url+featured_image_url
    mars_info["featured_image_URL"]=featured_image_url


    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(2)

    html=browser.html
    tweet_soup = BeautifulSoup(html, 'html.parser')

    mars_weather=tweet_soup.find('div',class_="js-tweet-text-container")
    Mars_weather=mars_weather.text.strip()
    mars_info["Latest_tweet"]=Mars_weather

    url = 'https://space-facts.com/mars/'
    # tables = pd.read_html(url)
    # DF=tables[0]
    Dict={'Equatorial Diameter':'6,792 km',
       'Polar Diameter': '6,752 km',
      'Mass':  '6.42 x 10^23 kg (10.7% Earth)',
     'Moons':'2 (Phobos & Deimos)',
     'Orbit Distance':'227,943,824 km (1.52 AU)',
     'Orbit Period':'687 days (1.9 years)',
     'Surface Temperature':'-153 to 20 °C',
     'First Record': '2nd millennium BC',
      'Recorded By':'Egyptian astronomers'
      }
    DF1 = pd.DataFrame.from_dict(Dict, orient='index')
    DF1=DF1.transpose()
    DF1.set_index('Equatorial Diameter',inplace=True)
#print(DF1)
    mars_info["table"]=Dict

    print(mars_info["table"])
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(2)

    html=browser.html
    soup_image_and_title = BeautifulSoup(html, 'html.parser')
    sections=soup_image_and_title.find_all('div', class_='item')
#Image_url = []
#title=[]
    Dicts={}
    img_url_Dict={}
    #List=[]

    for section in sections:
        Dicts={'title':section.find('img')['alt'].strip(),
            'img_url':section.find('img')['src'].strip()}
        img_url_Dict.update(Dicts)

    mars_info["dictionary with the image url"]=img_url_Dict

    browser.quit()

    return mars_info