from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver_path = "C:/chromedriver/chromedriver.exe"
service = ChromeService(executable_path=driver_path)
browser = webdriver.Chrome(service=service)
# Replace with the URL of the page containing the checkboxes
url = "https://stevensgrad.campuslabs.com/engage/actioncenter/organization/business-intelligence-analytics-club/roster/roster/pending"
browser.get(url)
print("Session ID:", browser.session_id)
session_id = browser.session_id

#checkboxes = browser.find_elements("xpath","//input[contains(@class, 'deleteInvitations-checkbox') and contains(@class, 'reinvite-checkbox') and @type='checkbox']")
#checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and contains(@class, 'deleteInvitations-checkbox') and contains(@class, 'reinvite-checkbox')]"))
wait = WebDriverWait(browser, 30)
checkbox_xpath="//input[@type='checkbox' and contains(@class, 'deleteInvitations-checkbox') and contains(@class, 'reinvite-checkbox')]"
checkboxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, checkbox_xpath)))

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

button_xpath = "//input[@type='submit' and contains(@class, 'mdl-button') and contains(@class, 'mdl-js-button') and contains(@class, 'mdl-button--raised')]" #works 1 time, not twice in a row
#button_xpath = '/html/body/meta name="viewport" content="initial-scale=1.0,/div[2]/div/div[3]/div/section/div[4]/div[2]/div/div[1]/div[1]/div/input'
#button = browser.find_element("xpath",button_xpath)
#button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath))) #works
button = wait.until(EC.visibility_of_element_located((By.XPATH, button_xpath)))
#button.click()
ActionChains(browser).move_to_element(button).click().perform()
