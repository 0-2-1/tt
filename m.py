from selenium import webdriver
from flask import Flask
import threading, time, os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/app/.apt/usr/bin/google_chrome"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path="/app/.chromedriver/bin/chromedriver", chrome_options=chrome_options)

app = Flask(__name__)


@app.route('/google')
def index():
    driver.get('https://google.com')
    return driver.page_source


@app.route('/')
def index():
    return __name__


threading.Thread(target=app.run, kwargs=dict(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))).start()

while 1:
    time.sleep(10)
