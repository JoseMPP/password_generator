import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'boss'
    start_urls = [
        'https://www.tiendaamiga.com.bo/tecnologia.html',
    ]

    def parse(self,response):
        cssName = 'a[class="product-item-link"]::text'
        cssPrice=
        for url in response.css(cssSel).getall():
            yield scrapy.Request(url,callback=self.parseProducts)




    def parseProducts(self,response):
        print('\n\n\n')
        print(response.url)
        cssSel='.product-tile-plp__gallery a::attr(href)'
        for productURL in response.css(cssSel).getall():
            yield response.follow(productURL,callback=self.parseProduct)
            print("------------------")

    def parseProduct(self,response):
        productName= response.css('.pdp-stage__header-title::text').get().strip()
        colorAvailable= response.css('.slides__container .slides__slide--color-selector::attr(title)').getall()
        colorAvailable=' | '.join(colorAvailable)
        picUrls=[]
        for i in response.css('.pdp-images__image::attr(data-src)').getall():
            picUrls.append(i.replace('&wid={width}&qlt={quality}',''))
        picUrls=' | '.join(picUrls)
        careInfo= response.css('.care-info__text ::text').getall()
        careInfo = ' | '.join(careInfo)
        yield {
            'Product Name' : productName,
            'Colors' : colorAvailable,
            'Pic Urls' : picUrls,
            'Care Infor': careInfo,
        }

