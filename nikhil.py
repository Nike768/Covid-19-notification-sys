from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon= "D:\python project\icon.ico",
        timeout = 6
    )
def getdata(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        # notifyMe("Nikhil","Lets stop this virus together")
        myHtml=getdata("https://covidindia.org/#")
        soup=BeautifulSoup(myHtml,"html.parser")
        # print(soup.prettify()
        mydatastr=""
        List=[]
        for td in soup.find_all('table')[0].find_all('td'):
            mydatastr = td.get_text()
            List.append(mydatastr)
        L2=[]
        i=0
        while i<36:
            L2.append(List[0:4])
            del List[0:4]
            i=i+1
        # print(L2)
        states=['Chandigarh','Uttarakhand','Punjab','Maharashtra']
        for i in L2:
            dataList=i
            if dataList[0] in states:
                print(dataList)
                ntitle='Cases of COVID-19 in INDIA'
                nmessage= f"State : {dataList[0]}\nConfirmed cases : {dataList[1]}\nRecoveries : {dataList[2]}\nDeaths : {dataList[3]} "
                notifyMe(ntitle,nmessage)
                time.sleep(2)
        time.sleep(60)





        
        
    