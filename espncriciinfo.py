import requests
import json
with open('news.txt','w') as f:
    for i in range(1,6):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page={i}'
        response = requests.get(url)
        data = json.loads(response.text)
        for news in data:
            f.write(news['author'] + '|' + news['summary'])
            f.write('\n')


