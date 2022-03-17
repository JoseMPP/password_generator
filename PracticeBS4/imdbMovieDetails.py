import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.imdb.com/chart/top/')
html = response.text
soup = BeautifulSoup(html,'html.parser')
tbody = soup.find('tbody',{'class':'lister-list'})
trs = tbody.find_all('tr')
movieName=input('Enter Movie Name:')
#recorrer lista de peliculas
for tr in trs:
    td = tr.find('td',{'class':'titleColumn'})
    imdbMovieName=td.a.string.strip()
    #Encontrar pelicula ingresada
    if imdbMovieName == movieName:
        movieId=td.a['href']
        movieUrl=f'https://www.imdb.com/{movieId}'
        response2 = requests.get(movieUrl)
        html = response2.text
        soup2 = BeautifulSoup(html, 'html.parser')
        director = soup2.find('li', {'class': 'ipc-metadata-list__item'})
        directorDetails = director.find('a')['href']
        directorUrl = f'https://www.imdb.com/{directorDetails}'
        print('Director name:',end='')
        for director in director.find_all('a'):
            print(director.text,end='   ')
        print('\n')
        #Obtener informacion de director
        response3 = requests.get(directorUrl)
        html = response3.text
        soup3 = BeautifulSoup(html, 'html.parser')
        knowfor = soup3.find('div', {'id': 'knownfor'})
        movieDivs = knowfor.find_all('div', {'knownfor-title'})
        print("Director movies recommendation:")
        for div in movieDivs:
            movieName2 = div.find('div', {'class': 'knownfor-title-role'})
            print(movieName2.a.string)
            print('----------')







