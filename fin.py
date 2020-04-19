import requests, io, time, datetime
from bs4 import BeautifulSoup
source = ["https://in.finance.yahoo.com/quote/%5EBSESN/history/","https://finance.yahoo.com/quote/%5ENYA/history?p=%5ENYA" ]
for i in range(0,2):
    URL = source[i]
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    html_page = requests.get(URL).text
    filename = "Data"+str(i)+".html"
    soup = BeautifulSoup (html_page, 'lxml')
    finance = soup.findAll("section", { "class" : "smartphone_Px(20px)" })
    open(filename, "w").close()
    with io.open(filename, "w",encoding="utf-8") as htmlfile:
            htmlfile.write(str(finance))
    htmlfile.close()
