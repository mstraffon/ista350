''' Author: Erin Berridge
    Course: ISTA350 SP23
    Final Project
'''

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

# PLOT 1 ------------ Most Common Monster Types
df1 = pd.read_csv(path + fname, usecols=[12], names=['Monster Type'], header=0)
top_monsters = df1['Monster Type'].value_counts()
top7_monsters = top_monsters.iloc[0:7]
y_pos = np.arange(7)

plt.figure('Image 1', figsize=(10,7.5), layout='constrained')
plt.bar(y_pos, top7_monsters.values, color='sandybrown')
plt.xticks(y_pos, top7_monsters.index, fontsize=12, rotation=25)

plt.title("Most Common Monster Types in Scooby Doo", fontsize=20)
plt.xlabel("Monster Type", fontsize=15, labelpad=15)
plt.ylabel("# of Monster Appearances in Scooby Doo", fontsize=15, labelpad=15)


# PLOT 2 ------------ Engagement vs. IMDB Rating w/ Regression
df2 = pd.read_csv(path + fname, usecols=[5,6], names=['IMDB', 'Engagement'], header=0)
df2 = df2.dropna()
df2 = df2.drop(df2[df2.Engagement > 300].index)

m, b = np.polyfit(df2['Engagement'], df2['IMDB'], deg=1)
xs = np.linspace(min(df2['Engagement']), max(df2['Engagement']), num=50)
model = sm.OLS(df2['IMDB'], df2['Engagement'])
results = model.fit()

plt.figure('Image 2', figsize=(10,7))
plt.plot('Engagement', 'IMDB', data=df2, linestyle='', marker='o', color='yellowgreen')
plt.plot(xs, m*xs + b, lw=3, color='darkorchid')
plt.xlim(0, 300)
plt.title("Engagement vs. IMDB Rating", fontsize=20)
plt.xlabel("Number of IMBD Reviews (Engagement)", fontsize=15, labelpad=15)
plt.ylabel("IMDB Episode Rating (1-10)", fontsize=15, labelpad=15)


# PLOT 3 ------------ IMDB Ratings by Network
df3 = pd.read_csv(path + fname, usecols=[2,5], names=['Network', 'IMDB'], header=0)
network_ratings = df3.groupby(['Network']).mean().sort_values(by=['IMDB'])
network_ratings = network_ratings.drop(network_ratings.index[[1,3,5,7,9]])
y_pos = np.arange(6)

plt.figure('Image 3', figsize=(10,7.5), layout='constrained')
plt.bar(y_pos, network_ratings['IMDB'], color='darkorchid')
plt.xticks(y_pos, network_ratings.index, fontsize=12, rotation=20)

plt.title("Average IMDB Ratings by Network", fontsize=20)
plt.xlabel("Network", fontsize=15, labelpad=15)
plt.ylabel("Average IMDB Rating (1-10)", fontsize=15, labelpad=15)

plt.show()