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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeSuAoKBxuiQNDs-M8YpDKJys9oqokRzyC-yQ0p710ig1UwcQ/viewform?fbzx=3067989463602548000")
#lucky_button = driver.find_element_by_css_selector("[name=btnI]")
submit = driver.find_elements_by_class_name("quantumWizButtonPaperbuttonLabel exportLabel")
#lucky_button.click()
print(driver.title)
# capture the screen
driver.get_screenshot_as_file("capture.png")