from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

soup.find_all('table')

# One way to pull the second table on the page
soup.find_all('table')[1]

# Another way to pull the second table on the page
soup.find('table', class_ = 'wikitable sortable')

table = soup.find_all('table')[1] 

world_titles = table.find_all('th')

world_table_titles = [titles.text.strip() for titles in world_titles]

df = pd.DataFrame(columns = world_table_titles)
print(df)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r"C:\Data Analytics & Science\Alex's Bootcamp\5. Python\2. Web Scraping in Python\companies.csv", index=False)

