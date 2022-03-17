import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'imdb'
    start_urls = [
        'https://www.imdb.com/chart/top/',
    ]

    def parse(self, response):
        for i in response.css('.titleColumn a'):
            movieName=i.css('::text').get()
            url = i.css('::attr(href)').get()

            dic={
                'movie':movieName,
            }
            yield response.follow(url,callback=self.parseInfo, meta=dic)
            print('\n')
            break

    def parseInfo(self,response):
        movieInformation = response.css('li.ipc-inline-list__item::text').getall()
        print('\n\n')
        print(response.meta)
        print(response.meta['movie'])
        print(movieInformation)