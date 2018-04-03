from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"\\chromedriver.exe"

# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("http://www.electricistas24horasbogota.com/contactenos")
#lucky_button = driver.find_element_by_css_selector("[name=btnI]")
nameField = driver.find_element_by_id("page93_inputsinglevalue1_inputsinglevalue1")
nameField.clear()
nameField.send_keys("Julian")

phoneField = driver.find_element_by_id("page93_inputsinglevalue2_phone")
phoneField.clear()
phoneField.send_keys("3142352865")

emailField = driver.find_element_by_id("page93_inputsinglevalue3_email")
emailField.clear()
emailField.send_keys("jularenas2@gmail.com")

comentarioField = driver.find_element_by_id("page93_inputsinglevalue4_inputsinglevalue4")
comentarioField.clear()
comentarioField.send_keys("Reparacion cableado hogar")

submit=driver.find_element_by_id("page93_formcontainer1_form")
submit.submit()


#lucky_button.click()
print(driver.title)
# capture the screen
driver.get_screenshot_as_file("capture.png")