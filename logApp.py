import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='w'
)

i=0
browser = webdriver.Chrome()
browser.get('https://www.amazon.com/')
browser.set_window_size(1920, 1080)
logging.info('Connection with Amazon succeeded')
browser.find_element(By.CSS_SELECTOR, "#nav-link-accountList .nav-icon").click()
browser.find_element(By.ID, "ap_email").click()
browser.find_element(By.ID, "ap_email").send_keys("pruebapytsel@gmail.com")
browser.find_element(By.CSS_SELECTOR, ".a-button-inner > #continue").click()
browser.find_element(By.ID, "ap_password").send_keys("d0xeado123")
browser.find_element(By.ID, "signInSubmit").click()
logging.info('Logging complete')
time.sleep(3)
browser.find_element(By.CSS_SELECTOR, "#nav-cart-text-container").click()
browser.find_element(By.NAME, "proceedToRetailCheckout").click()
browser.find_element(By.CSS_SELECTOR, ".os-primary-action-button-text").click()
time.sleep(3)
while i < 6:
    browser.find_element(By.CSS_SELECTOR, "#address-ui-widgets-form-submit-button .a-button-input").click()
    time.sleep(1)
    i += 1
    logging.info('Address not found')
browser.get('https://pytsel.atlassian.net/jira/software/projects/SCRUM/boards/2/backlog')
logging.info('Connection with JIRA completed')
browser.find_element(
    By.CSS_SELECTOR, "#google-auth-button").click()
browser.find_element(
    By.CSS_SELECTOR, "#identifierId").send_keys("pruebapytsel@gmail.com")
browser.find_element(
    By.CSS_SELECTOR, "#identifierNext > div > button").click()
time.sleep(2)
browser.find_element(
    By.NAME, "password").send_keys("d0xeado123")
browser.find_element(
    By.CSS_SELECTOR, "#passwordNext > div > button").click()
logging.info('Successfully logged in JIRA')
time.sleep(6)
browser.find_element(
    By.CSS_SELECTOR, "#ak-main-content > div > div > div.mhz6kn-1.Vtnnc > div.sc-8goq7c-0.boBVXp > div > div.sc-1boey8w-0.dQUaRQ > div.sc-1boey8w-3.cHpPxl > span > div > div > button").click()
time.sleep(2)
browser.find_element(
    By.CSS_SELECTOR, "#ak-main-content > div > div > div.mhz6kn-1.Vtnnc > div.sc-8goq7c-0.boBVXp > div > div.sc-1boey8w-0.dQUaRQ > div.sc-1boey8w-3.cHpPxl > span > div > div.qfnahh-0.dmWbPJ > form > div > div.qfnahh-3.jYHFdo > div > div > button").click()
browser.find_element(
    By.CSS_SELECTOR, "#react-select-2-option-1 > div").click()
time.sleep(1)
browser.find_element(
    By.CSS_SELECTOR, "#ak-main-content > div > div > div.mhz6kn-1.Vtnnc > div.sc-8goq7c-0.boBVXp > div > div.sc-1boey8w-0.dQUaRQ > div.sc-1boey8w-3.cHpPxl > span > div > div.qfnahh-0.dmWbPJ > form > div > div.qfnahh-4.doGKLo > div > textarea").send_keys("Problem requesting address")
browser.find_element(
    By.CSS_SELECTOR, "#ak-main-content > div > div > div.mhz6kn-1.Vtnnc > div.sc-8goq7c-0.boBVXp > div > div.sc-1boey8w-0.dQUaRQ > div.sc-1boey8w-3.cHpPxl > span > div > div.qfnahh-0.dmWbPJ > form > div > div.qfnahh-4.doGKLo > div > textarea").send_keys(Keys.ENTER)
logging.info('New bug added successfully')
time.sleep(200)