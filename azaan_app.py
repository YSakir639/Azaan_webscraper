from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

class Azaan:
    def __init__(self) -> None:
        self.weburl = "https://www.attaqwa.co.uk/" 
        self.request = urlopen(self.weburl)
        self.html_page = self.request.read()
        self.request.close()
        self.page_soup = soup(self.html_page,"html.parser")
        self.five_salah_time =  self.page_soup.find_all('td',{"class":"begins"})
    def get_salah_time(self,salah:int):
        salah -= 1
        salah =  self.five_salah_time[salah].text
        if "am" in salah:
            salah = salah.replace(" am",":AM")
        elif "pm" in salah:    
            salah = salah.replace(" pm",":PM")
        return salah
    def get_jummah_time(self):
        return self.page_soup.find_all("td",{"class":"jamah"})[11].text.split()[1] + ":PM"





