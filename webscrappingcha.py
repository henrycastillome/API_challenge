import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get ('https://www.census.gov/quickfacts/newyorkcitynewyork/').text

soup=BeautifulSoup (response, 'html.parser')

tables=soup.find_all('table')

#find how many tables are in that website
print(len(tables))

matching=pd.read_html(response, match='New York', flavor='bs4')

print(matching)
