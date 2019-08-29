from bs4 import BeautifulSoup
import requests
import re

def linkMinus(fullUrl):
  url = fullUrl.replace("https://www.","")
  return url

def scrape(data):
    l = []
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
    initSite['id'] = 0
    initSite['category'] = url
    initSite['name'] = url
    initSite['value'] = num
    initSite['label'] = url
    initSite['linkMinus'] = url

    l.append(initSite)

    num = 1

    for item in all_links:
        d = {}
        link = item.attrs['href']
        if link[0] == '/':
          link = base_url + link
        d['id'] = num
        d['category'] = url
        d['name'] = link
        d['value'] = num
        d['label'] = link
        # d['linkMinus'] = linkMinus(link)
        num = num + 1

        # CTC - uncomment below if you want to print every URL to console
        # print(link)

        l.append(d)

    return l
    # return data


if __name__ == "__main__":
    print(scrape())