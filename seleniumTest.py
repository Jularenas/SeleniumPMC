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

def electricistas24Horas(name,phone,email,desc):
 driver.get("http://www.electricistas24horasbogota.com/contactenos")
 #lucky_button = driver.find_element_by_css_selector("[name=btnI]")
 nameField = driver.find_element_by_id("page93_inputsinglevalue1_inputsinglevalue1")
 nameField.clear()
 nameField.send_keys(name)

 phoneField = driver.find_element_by_id("page93_inputsinglevalue2_phone")
 phoneField.clear()
 phoneField.send_keys(phone)

 emailField = driver.find_element_by_id("page93_inputsinglevalue3_email")
 emailField.clear()
 emailField.send_keys(email)

 comentarioField = driver.find_element_by_id("page93_inputsinglevalue4_inputsinglevalue4")
 comentarioField.clear()
 comentarioField.send_keys(desc)

 submit=driver.find_element_by_id("page93_formcontainer1_form")
 print("-------------")
 print("-------------")
 submit.submit()


 #lucky_button.click()
 print(driver.title)
 # capture the screen
 driver.get_screenshot_as_file("captureElectricistas24Horas.png")
 
def expertoYa(name,phone,email,desc,dir,now,date,time):
 print("ENTRE AL METODO") 
  
 driver.get("https://www.expertoya.com/")
 print("ENTRE A EXPERTOYA")
 print(driver.title)
 #lucky_button = driver.find_element_by_css_selector("[name=btnI]")
 nameField = driver.find_element_by_id("edit-field-user-name-und-0-value")
 nameField.clear()
 nameField.send_keys(name)

 phoneField = driver.find_element_by_id("edit-field-phone-und-0-value")
 phoneField.clear()
 phoneField.send_keys(phone)

 emailField = driver.find_element_by_id("edit-mail")
 emailField.clear()
 emailField.send_keys(email)

 comentarioField = driver.find_element_by_id("edit-body-und-0-value")
 comentarioField.clear()
 comentarioField.send_keys(desc)
 
 direccionField= driver.find_element_by_id("edit-title")
 direccionField.send_keys(dir)
 
 ya= driver.find_element_by_id("edit-field-cuando-und-0")
 
 programada=driver.find_element_by_id("edit-field-cuando-und-1")
 
 dateField=driver.find_element_by_id("edit-field-service-date-und-0-value-datepicker-popup-0")
 timeField=driver.find_element_by_id("edit-field-service-date-und-0-value-timepicker-popup-1")
 
 
 if(now==1):
   ya.click()
 else:
   programada.click()
   dateField.send_keys(date)
   timeField.send_keys(time)
   
   
 terms= driver.find_element_by_id("edit-legal-accept")
 submit=driver.find_element_by_id("edit-submit")
 
 print("-------------")
 print("-------------")
 terms.click()
 submit.click()
 print(driver.title)
 element2 = driver.find_element_by_id("main-content")
 element3=element2.find_element_by_id("block-views-user-listing-block-2")
 print (element2.get_attribute('innerHTML'))

# element2.find_element_by_xpath(".//span[@class='tecnico_ya']").getText() 
 


 #lucky_button.click()
 print(driver.title)
 # capture the screen
 driver.get_screenshot_as_file("captureExpertoYa.png")
electricistas24Horas("Ricardo","3000000000","t.kavanagh@uniandes.edu.co","Necesito que arrglen a mi perro aaaaaaaaaaaaaaaaaaaaaa xp")
expertoYa("Ricardo","3000000000","t.kavanagh@uniandes.edu.co","necesito un cerrajero ","cll 34sur#51-22",1,"9 Mayo 2018","20")