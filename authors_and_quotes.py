import requests
import csv
authors=[]
quotes=[]
for i in range(1,11):
    url = f'https://quotes.toscrape.com/page/{i}/'
    site_request = requests.get(url)
    html = site_request.text

    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            quote = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
            quote=quote.strip()
            quotes.append(quote)
        if '<span>by <small class="author" itemprop="author">' in line:
            author = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            author=author.strip()
            authors.append(author)

with open('quotes.csv','w',encoding='utf-8') as f:
    for content in zip(authors, quotes):
        f.write(content[0] + ','+ '"' + content[1] + '"')
        f.write('\n')







