import os
import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
from config import site_link

class Weather:
    
    def saveToExcel(self):
        lis = self.worldWideReport()
        df = pd.DataFrame(data = lis,columns = ['Country','City','Temparature-in-Celcius','Extraction-Datetime'])
        df.to_csv('weather.csv')
        print(f"Data saved in {os.getcwd()}\\weather.csv")
        
    def worldWideReport(self):
        try:
            url= 'https://www.timeanddate.com/weather/?sort=1&low=c'
            page = requests.get(url)
            soup =  BeautifulSoup(page.content,'html.parser')
            table = soup.find_all('tr')
            weatherlist = []
            for i in range(1,len(table)):
                text = table[i].find_all('td')
                city_and_country = text[0].get_text()
                temp = text[len(text)-1].get_text().translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+°C\xa0"}).strip()
                city_country_split = city_and_country.split(',')
                if(len(city_country_split) == 2):
                    city = city_country_split[1].replace('*','').strip()
                else:
                    city = city_country_split[2].replace('*','').strip()
                country = city_country_split[0].replace('*','').strip()
                weatherlist.append([country,city,temp,str(datetime.now())])
            return weatherlist
        
        except Exception as e:
            print("Extraction Error: Please try after some time ...")
                
        