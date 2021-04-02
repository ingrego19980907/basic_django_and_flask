import requests
from bs4 import BeautifulSoup

ITEMS = 100
URL = f'https://hh.ru/search/vacancy?st=searchVacancy&text=Python&items_on_page={ITEMS}'
HEADERS = {
    'Host': 'hh.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
  }

def extract_max_page():
  
  

  hh_request = requests.get(URL , headers=HEADERS)

  pages = []

  hh_soup = BeautifulSoup(hh_request.text, 'html.parser')
  paginaror = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})

  for page in paginaror:
    pages.append(int(page.find('a').text))

  return pages[-1]

def extract_hh_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f'{URL}&page=0', headers=HEADERS)
  print(result.status_code)
  soup = BeautifulSoup(result.text, 'html.parser')
  results = soup.find_all('div', {'class': 'vacancy-serp-item'})
  for result in results:
    title = result.find('a').text
    company = result.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).find('a').text
    print(company)

  return jobs