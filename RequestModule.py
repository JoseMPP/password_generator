import requests
site_request = requests.get('https://quotes.toscrape.com/')
html = site_request.text
with open('quotes1.txt','w',encoding='utf-8') as f:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            line= line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
            line = line.strip()
            print(line)
            f.write(line)
            f.write('\n')
