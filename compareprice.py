#this script will compare price of a product on amazon and flipkart and display the better one
#be specific with the product name 
import sys,requests,bs4,webbrowser,re
print("----------comparing ...-----------")
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
aAmountlist=asoup.select('#priceblock_ourprice')
a=False
f=False
#price on amazon is:
try:
  print('amazon price------> '+aAmountlist[0].getText())
  atmp=aAmountlist[0].getText().split('.')
  acost=re.sub('[^0-9]','',atmp[0])
  acost=int(acost)
  a=True
except: #product not found
  print("product not found on amazon")
#scraping the flipkart page
#print('wait wait...')
flist=fsoup.select('.r a')
freq=requests.get('http://google.com'+flist[0].get('href'))
fsoup=bs4.BeautifulSoup(freq.text)
fAmountlist=fsoup.select('._1vC4OE._3qQ9m1')
try:
  print('flipkart price----->'+fAmountlist[0].getText())
  fcost=re.sub('[^0-9]','',fAmountlist[0].getText()) #price on flipkart
  fcost=int(fcost)
  f=True
except:
  print("product not found on flipkart")

if a and f:
  if acost<=fcost:  #:P
      print("fetching amazon page...")
      webbrowser.open('http://google.com'+alist[0].get('href'))
  else:
      print("fetching flipkart page..")
      webbrowser.open('http://google.com'+flist[0].get('href'))

elif a:
  print("fetching amazon page...")
  webbrowser.open('http://google.com'+alist[0].get('href'))    

elif f:
  print("fetching flipkart page..")
  webbrowser.open('http://google.com'+flist[0].get('href'))  

