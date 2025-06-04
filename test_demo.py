import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
chrome_path = os.path.join(os.path.abspath(__file__), '..', 'chromedriver.exe')

@pytest.fixture(scope='module')
def setup_browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_hiring_button(setup_browser):
    driver = setup_browser
    driver.get('https://tier4.jp/')
    try:
        driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
    except:
        pass
    time.sleep(10)
    buttonHiring = driver.find_element(By.CLASS_NAME, 'btnsimple')
    assert buttonHiring.text == '2026年新卒採用募集中'

def test_hiring_page_title(setup_browser):
    driver=setup_browser
    driver.get('https://tier4.jp/')
    try:
        driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
    except:
        pass
    time.sleep(10)
    driver.find_element(By.CLASS_NAME, 'btnsimple').click()
    pageTitle = driver.find_element(By.CLASS_NAME, 'requisition-header__name')
    assert pageTitle.text == '0001_新卒 エンジニア職 / New graduate (Engineer)'
    
