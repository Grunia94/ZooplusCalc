from bs4 import BeautifulSoup
import requests 
import xlsxwriter

# 1. Retrieve HTML and create BeautifulSoup object
response = requests.get("https://www.w3schools.com/html/html_tables.asp")
soup = BeautifulSoup(response.text,features="html.parser")
# 2. Find the table and extract headers and rows:
table = soup.find('table', {"id": "customers"})
print(table)