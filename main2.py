from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
#notify function to generate notifications
def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon= "D:\python project\icon.ico",
        timeout = 6
    )
#function to extract  data from url address
def getdata(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    myHtml=getdata("https://prsindia.org/covid-19/cases")
    # Making soup of all html data extracted from url
    soup=BeautifulSoup(myHtml,"html.parser")
    # print(soup.prettify()
    mydatastr=""
    List=[]
    for td in soup.find_all('table')[0].find_all('td'):
        mydatastr = td.get_text()
        List.append(mydatastr)
    del List[0:6]
    #print(List)
    L2=[]
    i=0
    while i<36:
            L2.append(List[0:6])
            del List[0:6]
            i=i+1
    # print(L2)
    # Name of the states for which the data  will be printed
    states=['Chandigarh','Uttarakhand','Punjab','Maharashtra']
    for i in L2:
        dataList=i
        if dataList[1] in states:
            print(dataList)
            ntitle='Cases of COVID-19 in INDIA'
            nmessage= f"State : {dataList[1]}\nConfirmed cases : {dataList[2]}\nRecoveries : {dataList[4]}\nDeaths : {dataList[5]} "
            notifyMe(ntitle,nmessage)
            time.sleep(2)
    #time.sleep(60)
           





        
        
    