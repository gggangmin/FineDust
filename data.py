import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib.parse
import codecs
from selenium import webdriver 

CommerceInfor = {}
pm10value_list = []
pm25value_list = []
o3value_list = []
so2value_list = []
pm10value24_list = []
expectation_list = []

stationName_list = ['강서구','양천구','구로구','영등포구','금천구','동작구','관악구','서초구','강남구','송파구','강동구','마포구','서대문구','은평구','종로구','중구','용산구','강북구','성북구','동대문구','성동구','노원구','중랑구','광진구','도봉구']

for stationName in stationName_list:
    urlStationName = urllib.parse.quote(stationName)
    url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName='+urlStationName+'&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=EAFfEKtlU%2B3B4huu4yz2Rg%2FaeRQdNAjw7%2FSR0b2KkkubMHVBZeynd3aYMD2bzR6eY1ox1WUXtVNRaNQb2GbkWQ%3D%3D&ver=1.3'
    req=requests.get(url)
    html=req.text
    soup=BeautifulSoup(html, 'html.parser')
    
    pm10value = soup.find_all('pm10value')
    if pm10value[0].text == '-':
        pm10value_list.append(str(20))
    else:
        pm10value_list.append(pm10value[0].text)
    
    
    pm25value = soup.find_all('pm25value')
    if pm25value[0].text == '-':
        pm25value_list.append(str(13))
    else:
        pm25value_list.append(pm25value[0].text)
    
    o3value = soup.find_all('o3value')
    if o3value[0].text == '-':
        o3value_list.append(str(0.02))
    else:
        o3value_list.append(o3value[0].text)
    
    so2value = soup.find_all('so2value')
    if so2value[0].text == '-':
        so2value_list.append(str(0.01))
    else:
        so2value_list.append(so2value[0].text)
    
    pm10value24 = soup.find_all('pm10value24')
    pm10value24_list.append(pm10value24[0].text)
    p = pm10value24[0].text
    pp = pm10value[0].text
    if p == '-':
        p = float(20)
    else:
        p = float(p)
        
    if pp == '-':
        pp = float(20)
    else:
        pp = float(pp)
    expectation_list.append(str(p+p-pp))
    

file = open('index.html','w',encoding="utf8")
file.close()

filea = open('A.html','r',encoding="utf8")
fileb = open('B.html','r',encoding="utf8")
file = open('index.html','w',encoding="utf8")

for line in filea:
    file.write(line)
file.write('        var arrM ='+str(pm10value_list)+';  \n')
file.write('        var arrC ='+str(pm25value_list)+';  \n')
file.write('        var arrO ='+str(o3value_list)+';  \n')
file.write('        var arrH ='+str(so2value_list)+';  \n')
file.write('        var arrN ='+str(pm10value24_list)+';  \n')
file.write('        var arrNN ='+str(expectation_list)+';  \n')
for line in fileb:
    file.write(line)
file.close()
filea.close()
fileb.close()

driver = webdriver.Chrome('C:/Users/user/Downloads/2학년 2학기/PL/먼지뭐지/chromedriver.exe') 
driver.implicitly_wait(3) 
driver.get('file:///C:/Users/user/Downloads/2%ED%95%99%EB%85%84%202%ED%95%99%EA%B8%B0/PL/%EB%A8%BC%EC%A7%80%EB%AD%90%EC%A7%80/index.html')
