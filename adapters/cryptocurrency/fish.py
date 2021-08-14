from bs4 import BeautifulSoup
import requests

url = 'https://old.polycat.finance/'

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
