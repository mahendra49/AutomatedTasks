#  opens several google search results

import requests, sys, webbrowser, bs4
print('Googling...')
#google it using command line 
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
#pass the html to bs4
soup=bs4.BeautifulSoup(res.text)
#get all anchor tags inside of class ".r" 
#see google search html code for more info 
#and store all the data in a list
links=soup.select('.r a') #all required list of data
#open at max 5 links
noOfLinks=min(5,len(links))
#opening the links in browser
for i in range(noOfLinks):
    webbrowser.open('http://google.com'+links[i].get('href'))
    
#done done done

