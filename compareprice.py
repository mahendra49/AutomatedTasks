# this script will compare prices of a product on amazon and flipkart and display the best one
#be specific with the product name 
import sys,requests,bs4,webbrowser,re
print("----------comparing prices...-----------")
#search google for the product
areq=requests.get('http://google.com/search?q='+'amazon '+''.join(sys.argv[1:]))
freq=requests.get('http://google.com/search?q='+'flipkart '+''.join(sys.argv[1:]))
asoup=bs4.BeautifulSoup(areq.text)
fsoup=bs4.BeautifulSoup(freq.text)
#I'm taking only the first link

#scraping the amazon page
alist=asoup.select('.r a') #select all the links 
#I'm selecting only the first link
areq=requests.get('http://google.com'+alist[0].get('href')) 
asoup=bs4.BeautifulSoup(areq.text)
aAmountlist=asoup.select('#priceblock_dealprice')
#price on amazon is:
print('amazon price------> '+aAmountlist[0].getText())
atmp=aAmountlist[0].getText().split('.')
acost=re.sub('[^0-9]','',atmp[0])
acost=int(acost)

#scraping the flipkart page
#print('wait wait...')
flist=fsoup.select('.r a')
freq=requests.get('http://google.com'+flist[0].get('href'))
fsoup=bs4.BeautifulSoup(freq.text)
fAmountlist=fsoup.select('._1vC4OE._3qQ9m1')
print('flipkart price----->'+fAmountlist[0].getText())
fcost=re.sub('[^0-9]','',fAmountlist[0].getText()) #price on flipkart
fcost=int(fcost)

if acost<=fcost:  #:P
    print("fetching amazon page...")
    webbrowser.open('http://google.com'+alist[0].get('href'))
else:
    print("fetching flipkart page..")
    webbrowser.open('http://google.com'+flist[0].get('href'))


