from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

# Scrap the data from property website
response = requests.get("https://homes.trovit.my/for-rent-bayan-lepas-apartment")
website = response.content

soup = BeautifulSoup(website, "html.parser")

all_addresses = [address.getText().title() for address in soup.find_all(name="a", class_="js-item-title")]
all_prices = [price.getText().strip() for price in soup.find_all(name="span", class_="amount")]
all_urls = [url["href"] for url in soup.find_all(name="a", class_="js-item-title")]

# Autofill the data in Google Sheet
chrome_driver_path = "C://Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

for n in range(len(all_urls) - 1):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScnEUZ50mVL7D-AuqIaW7dlESDupuxMxotb1tL19j1jxc42OQ/viewform"
               "?usp=sf_link")

    time.sleep(2)
    address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                 '1]/div/div[1]/input')
    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')
    url_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                             '1]/div/div[1]/input')

    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')

    address_input.send_keys(all_addresses[n])
    price_input.send_keys(all_prices[n])
    url_input.send_keys(all_urls[n])
    submit_btn.click()
