from bs4 import BeautifulSoup
import requests
response = requests.get('https://www.imdb.com/chart/top/')
html = response.text
soup = BeautifulSoup(html,'html.parser')
tbody = soup.find('tbody',{'class':'lister-list'})
trs = tbody.find_all('tr')
for tr in trs:
    td = tr.find('td',{'class':'titleColumn'})
    movieId = td.a['href']
    movieUrl = f'https://www.imdb.com/{movieId}'
    response2 = requests.get(movieUrl)
    html = response2.text
    soup2 = BeautifulSoup(html, 'html.parser')
    info = soup2.find('ul', {'class': 'TitleBlockMetaData__MetaDataList-sc-12ein40-0'})
    print(td.a.string)
    for li in info.find_all('li'):
        print(li .text)

    print('--------------------------------')