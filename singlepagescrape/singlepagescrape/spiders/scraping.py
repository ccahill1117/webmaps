from bs4 import BeautifulSoup
import requests


def scrape():
    l = []
    base_url = 'https://www.nytimes.com'
    print(base_url)

    # Request URL and Beautiful Parser
    html = requests.get(base_url)

    soup = BeautifulSoup(html.text, 'html.parser')

    all_links = soup.find_all('a', href=True)
    print(len(all_links))

    for item in all_links:
        d = {}

        link = item.attrs['href']
        d[link] = link
        # CTC - uncomment below if you want to print every URL to console
        # print(link)

        # image
        # product_image = item.find("href")
        # image = image.text.replace('\n', "").strip()
        # product_image = product_image['src']
        # d['product_image'] = product_image

        # # name & link
        # product_name = item.find("a", {"class":"product__name"})
        # product_link = 'https://www.bukalapak.com' + str(product_name.get('href'))
        # product_name = product_name.text.replace('\n', "").strip()
        # d['product_link'] = product_link
        # d['product_name'] = product_name

        # # price
        # product_price = item.find("span", {"class":"amount"})
        # product_price = product_price.text.replace('\n', "").strip()
        # d['product_price'] = 'Rp' + product_price

        # # review
        # product_review = item.find("a", {"class":"review__aggregate"})
        # try:
        #     product_review = product_review.text
        #     d['product_review'] = int(product_review)
        # except:
        #     d['product_review'] = 0

        # link
        # product_link = item.find("a", {"class":"product-media__link"}, href=True)
        # product_link = 'https://www.bukalapak.com' + str(product_link.get('href'))
        # d['product_link'] = product_link

        l.append(d)

    return l


if __name__ == "__main__":
    print(scrape())