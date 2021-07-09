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


def signup(email, password):
    pass


def login(email, password, signup=True):
    driver.get('https://id.heroku.com/login')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
    driver.find_element_by_id("email").send_keys(email)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
    driver.find_element_by_id("password").send_keys(password + Keys.ENTER)

    s = driver.page_source
    if '<h2 class="h3">Secure Your Account</h2>' in s:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mfa-later"]/button')))
        driver.find_element_by_xpath('//*[@id="mfa-later"]/button').click()
    # elif notfound and signup:
    #     signup()




@app.route('/heroku')
def index():
    login("mohammadia633@gmail.com", "moh@mm@dsh@hi0123")
    driver.get('https://dashboard.heroku.com/new-app')

    xpath = '/html/body/div[5]/main/div[2]/div[2]/form/div/div[2]/div/input'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.find_element_by_xpath(xpath).send_keys("seleni2")
    time.sleep(5)
    xpath = '/html/body/div[5]/main/div[2]/div[2]/form/div/button[2]'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.find_element_by_xpath(xpath).click()

    driver.get('https://dashboard.heroku.com/logout')
    login("mohammadia633@gmail.com", "moh@mm@dsh@hi0123", signup=False)
    driver.get('https://dashboard.heroku.com/apps/seleni/settings')

    try:
        xpath = '/html/body/div[5]/main/div[2]/div[2]/ul/li[8]/div/div[2]/p/span/button'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        driver.find_element_by_xpath(xpath).click()

        xpath = '/html/body/div[4]/div[1]/div/div/div[2]/div/div/input'
        driver.find_element_by_xpath(xpath).send_keys("seleni")
        xpath = '/html/body/div[4]/div[1]/div/div/div[3]/button[2]'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        driver.find_element_by_xpath(xpath).click()

        #deleteaccount
    except Exception:
        pass

    # deploy

    return driver.page_source


@app.route('/')
def xxx():
    return str(r)


#https://www.heroku.com/deploy/?template=https://github.com/0-2-1/tt
threading.Thread(target=app.run, kwargs=dict(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))).start()

while 1:
    time.sleep(10)
