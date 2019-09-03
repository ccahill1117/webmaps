from bs4 import BeautifulSoup
import requests
import re

def linkMinus(fullUrl):
  url = fullUrl.replace("https://www.","")
  return url

def scrape(data):
    links = []
    connects = []
    params = data['params']
    url = params['links']
    print(data)
    base_url = 'https://www.' + url 
    print(url)

    # Request URL and Beautiful Parser
    html = requests.get(base_url)

    soup = BeautifulSoup(html.text, 'html.parser')

    all_links = soup.find_all('a', href=True)
    print(len(all_links))

    num = 0 

    # create initial starting point
    initSite = {}
    initSite['id'] = num
    initSite['category'] = 'a'
    initSite['name'] = url
    initSite['value'] = 0
    # initSite['label'] = url
    # initSite['linkMinus'] = url

    links.append(initSite)

    num = 1

    for item in all_links:
        d = {}
        link = item.attrs['href']
        shortLink = link[-10:]
        if link[0] == '/':
          link = base_url + link
        d['id'] = num
        d['category'] = 'a'
        d['name'] = shortLink
        d['value'] = num
        # d['label'] = link

        # CTC append each link object 'd' to links array
        links.append(d)

        # CTC append each connection 'c' to connects array
        c = {}
        normalStyle = { 'normal' : { 'color': 'red',
                          'width' : '3.5'
        }}
        labelItem = { 'normal' : { 'show' : True ,
                                  'width' : '3.5'
        
        
        } }

        c['source'] = 0
        c['target'] = num
        c['weight'] = 2
        c['lineStyle'] = labelItem
        # c['label'] = labelItem
        connects.append(c)
        num = num + 1

    dataReturn = {}
    dataReturn['links'] = links
    dataReturn['connects'] = connects
    return dataReturn
   


if __name__ == "__main__":
    print(scrape())