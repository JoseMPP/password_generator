import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com',
    ]

    def parse(self, response):
        for div in response.css('.quote'):
            quote = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('a.tag::text').getall()
            yield  {
                'quote':quote.replace('“','"').replace('”','"'),
                'author': author,
                'tags':tags
            }
        next_page_url = response.css('li.next a::attr(href)').get()
        print(tags)
        print('---------------')
        print(next_page_url)
        if next_page_url:
            yield response.follow(next_page_url,callback=self.parse)
        else:
            print("\n\n\n\n Last page")


        # print("Response From Server:",response.url)
        # print("Status From Server:", response.status)
        # print("Header", response.headers)
        # print("Body from server",type(response.body))
        # print("VALUE FROM HEADER",response.headers.get('Server'))
        # print("Value FROM Header",response.headers.get('Content-Type'))
