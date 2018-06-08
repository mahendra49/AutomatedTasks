#this will open list of all available products on amazon ..one per tab
#run python3 filename.py "product name without quotes"

import bs4,requests,webbrowser,sys
print("fetching products....")
#fetch results using google
req=requests.get('https://www.google.com/search?q='+'amazon '+''.join(sys.argv[1:]))
webbrowser.open('https://www.google.com/search?q='+'amazon '+''.join(sys.argv[1:]))
# opening the first link first link to amazon
req.raise_for_status()
soup=bs4.BeautifulSoup(req.text)
# you can open multiple links as per requirement
alist=soup.select('.r a')
print(alist[0].get('href'))
webbrowser.open('http://google.com' + alist[0].get('href'))
proreq=requests.get('http://google.com' + alist[0].get('href'))
prosoup=bs4.BeautifulSoup(proreq.text)
prolist=prosoup.select('li a')
#open at max 5 best results
prolen=min(5,len(prolist))
#webbrowser.open('http://google.com' + alist[0].get('href'))
for i in range(prolen):
    webbrowser.open('https://www.amazon.in/'+prolist[i].get('href'))
