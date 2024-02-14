from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd;

url = "https://usa.ipums.org/usa-action/variables/OCC1950#codes_section"  # Replace with actual URL
driver = webdriver.Chrome()  # Or use your preferred browser
driver.get(url)

# Wait for the table to load (adjust the condition as needed)
table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dataTable")) 
)

html_source = driver.page_source
driver.quit()  # Close the browser

soup = BeautifulSoup(html_source, 'html.parser')

outer_container = soup.find('div', id='dataTable')
table = outer_container.find('table', attrs={'class': 'variablesList'})  # Adjust targeting as needed


column1_data = []
column2_data = []

for row in table.find_all('tr', attrs={'class': 'variables'}):
    cells = row.find_all('td')  # Change to 'th' if your data is in the header
    if len(cells) >= 2:  # Make sure enough columns exist
        column1_data.append(cells[0].text.strip())
        column2_data.append(cells[1].text.strip())

# Step 5: Store or utilize the data
data = { 'OCC': column1_data, 'Occupation': column2_data }
df = pd.DataFrame(data)
df.to_csv('./data/occ1950.tsv', sep='\t', index=False) 
print(df)
