from bs4 import BeautifulSoup
import requests
response = requests.get('https://quotes.toscrape.com/')
html = response.text
soup = BeautifulSoup(html,'html.parser')
with open('authors.csv','w') as f:
    for tag in soup.find_all('small'):
        print(tag.string)
        f.write(tag.string)
        f.write('\n')
        
