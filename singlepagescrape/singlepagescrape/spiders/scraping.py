from bs4 import BeautifulSoup
import requests


def scrape(url):
    l = []
    base_url = 'https://www.' + url + '.com'
    print(base_url)

    # Request URL and Beautiful Parser
    html = requests.get(base_url)

    soup = BeautifulSoup(html.text, 'html.parser')

    all_links = soup.find_all('a', href=True)
    print(len(all_links))

    num = 0

    for item in all_links:
        d = {}
        link = item.attrs['href']
        d[num] = link
        num = num + 1

        # CTC - uncomment below if you want to print every URL to console
        # print(link)

        l.append(d)

    return l


if __name__ == "__main__":
    print(scrape())