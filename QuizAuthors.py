import requests
site_request = requests.get('https://quotes.toscrape.com/')
html = site_request.text

with open('Authors.txt','w') as f:
    for line in html.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in line:
            author = line.replace('<span>by <small class="author" itemprop="author">“','').replace('</small>','')
            author = author.strip()
            f.write(author)
            f.write('\n')
