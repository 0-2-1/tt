from selenium import webdriver
from flask import Flask
import threading, time, os, random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/app/.apt/usr/bin/google-chrome"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path="/app/.chromedriver/bin/chromedriver", chrome_options=chrome_options)

r= random.randint(0,100)
app = Flask(__name__)


@app.route('/heroku')
def index():
    driver.get('https://id.heroku.com/login')

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "email")))
    driver.find_element_by_id("email").send_keys("mohammadia633@gmail.com")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "password")))
    driver.find_element_by_id("password").send_keys("moh@mm@dsh@hi0123" + Keys.ENTER)

    s = driver.page_source
    if '<h2 class="h3">Secure Your Account</h2>' in s:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mfa-later"]/button')))
        driver.find_element_by_xpath('//*[@id="mfa-later"]/button').click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'ember36')))
    driver.find_element_by_id('ember36').click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "ember69")))
    driver.find_element_by_id("ember69").send_keys("seleni")
    time.sleep(5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'ember77')))
    driver.find_element_by_id('ember77').click()
    return driver.page_source


@app.route('/')
def xxx():
    return str(r)


#https://www.heroku.com/deploy/?template=https://github.com/0-2-1/tt
threading.Thread(target=app.run, kwargs=dict(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))).start()

while 1:
    time.sleep(10)
