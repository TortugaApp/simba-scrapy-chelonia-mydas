import pandas as pd
import scrapy
import urllib.request
import ssl
import os
import shutil

URL_BASE = "https://segurogis.petrobras.com.br"
URL_SIMBA_BASE = URL_BASE + "/simba/web/sistema/pmp/1/individualfaunaoccurrence/"
BASE_OS_TURTLE_PATH = "turtle/"

DF = pd.read_excel('Ocorrências de fauna alvo individual 12_02_2019 20_01.xlsx')

IS_CARCACA_RANGE = DF["Condição da carcaça"] <= 3

ssl._create_default_https_context = ssl._create_unverified_context

class SimbaSpider(scrapy.Spider):
    name = "SimbaSpider"
    
    #According to the rows of excel
    def start_requests(self):
        if os.path.exists(BASE_OS_TURTLE_PATH):
            shutil.rmtree(BASE_OS_TURTLE_PATH, ignore_errors=True)
            
        os.makedirs(BASE_OS_TURTLE_PATH)
        
        for index, row in DF[IS_CARCACA_RANGE].iterrows():
            yield scrapy.Request(URL_SIMBA_BASE + str(row['Código']), self.parse)
            #break
         

    def parse(self, response):
        imgs = response.css(".fancybox-button img").xpath("@src")
        url = response.request.url.split("/")[-1]
        path = BASE_OS_TURTLE_PATH + str(url)
        if not os.path.exists(path):
            os.makedirs(path)
        
        for img in imgs:
            src = img.get()
            print(src)
            print(src.split("/")[-1])
            urllib.request.urlretrieve(url = URL_BASE + src, filename = path + "/" +src.split("/")[-1])
