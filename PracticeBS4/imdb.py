import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.imdb.com/chart/top/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
tbody = soup.find('tbody',{'class':'lister-list'})
trs = tbody.find_all('tr')
with open('idmb_top.csv','w') as f:
    for table_row in trs:
        td_title = table_row.find('td',{'class':'titleColumn'})
        td_rating = table_row.find('td',{'class':'ratingColumn imdbRating'})
        f.write(td_title.a.string + '|' + td_title.span.string + '|' + td_rating.strong.string)
        f.write('\n')
        print('"' + td_title.a.string,td_title.span.string,td_rating.strong.string)