from selenium import webdriver
from selenium.webdriver.common.by import By
import time, requests
import pandas as pd, matplotlib.pyplot as plt, numpy as np
import statsmodels.api as sm


# --- Web Scraping ------
url = 'https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2F'

browser = webdriver.Chrome()
browser.get(url)
login_fields = browser.find_elements(By.CLASS_NAME, 'mdc-text-field__input')
login_fields[0].send_keys('eriberridge@gmail.com')
login_fields[1].send_keys('dummypass')
time.sleep(1)
loginBtn = browser.find_element(By.CSS_SELECTOR, '.sc-hVkBjg.hLHXAF')
loginBtn.click()
time.sleep(2)
scooby = 'https://www.kaggle.com/datasets/williamschooleman/scoobydoo-complete'
browser.get(scooby)
get_here = browser.find_element(By.CSS_SELECTOR, '.sc-gVCVku.dAnUcv')
time.sleep(1)
browser.execute_script("arguments[0].scrollIntoView();", get_here)
time.sleep(2)
dwnldBtn = browser.find_element(By.CSS_SELECTOR, '.rmwc-icon.rmwc-icon--ligature.google-material-icons.sc-BKAtq.fmysTT')
dwnldBtn.click()
time.sleep(3)

# Plotting ----------------------
path = '/Users/erinberridge/Downloads/'
fname = 'Scooby-Doo Complete - Episode List - Update 10 19 21.csv'
df1 = pd.read_csv(path + fname, usecols=[12], names=['Monster Type'], header=0)
print(df1.head())