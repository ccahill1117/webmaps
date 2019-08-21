import scrapy

class LinkCheckerSpider(scrapy.Spider):
    name = 'link_checker'
    allowed_domains = ['www.nytimes.com']
    start_url = ['https://www.nytimes.com']

    def parse(self, response):
        """ Main function that parses downloaded pages """
        # Print what the spider is doing
        print(response.url)
        # Get all the <a> tags
        a_selectors = response.xpath("//a")
        # Loop on each tag
        for selector in a_selectors:
            # Extract the link text
            text = selector.xpath("text()").extract_first()
            # Extract the link href
            link = selector.xpath("@href").extract_first()
            # Create a new Request object
            request = response.follow(link, callback=self.parse)
            # Return it thanks to a generator
            yield request
