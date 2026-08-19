import requests
import panda as pd
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

jobData = []
results = soup.find_all('div', class_='column is-half')

for result in results:
    jobTitle = result.find('h2', class_='title is-5').text.strip()
    companyName = result.find('h3', class_='subtitle is-6 company').text.strip()
    location = result.find('p', class_='location').text.strip()
    jobDetailPageUrl = result.find('a', class_='card-footer-item', string='Apply', href=True)['href'].strip()
    jobData.append({
        'title': jobTitle,
        'company': companyName,
        'location': location,
        'url': jobDetailPageUrl
    })

df = pd.DataFrame(jobData)
print(df)
