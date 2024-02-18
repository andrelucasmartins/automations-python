import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

titles = driver.find_elements(By.XPATH, "//a[@class='nome-produto']")
prices = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")

# # creating workbook
workbook = openpyxl.Workbook()
# # creating products sheet
workbook.create_sheet("products")
# # selecting products sheet
sheet_products = workbook['products']

sheet_products["A1"].value = "Product"
sheet_products["B1"].value = "Price"

# Appending titles and prices into products sheet
for title , price in zip(titles, prices):
  sheet_products.append([title.text, price.text])

workbook.save("products.xlsx")