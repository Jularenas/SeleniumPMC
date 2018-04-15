from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
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
  
 driver.get("https://www.expertoya.com")
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
 
 driver.get_screenshot_as_file("captureExpertoYaSinEnviar.png")
 
 print("-------------")
 print("-------------")
 terms.click()
 submit.click()
 print(driver.title)
 element2 = driver.find_element_by_id("main-content")
 #element3=element2.find_element_by_id("block-views-user-listing-block-2")
 print (element2.get_attribute('innerHTML'))

# element2.find_element_by_xpath(".//span[@class='tecnico_ya']").getText() 
 


 #lucky_button.click()
 print(driver.title)
 # capture the screen
 driver.get_screenshot_as_file("captureExpertoYa.png")
 
 
# def doctorSolucion(name,phone,phone2,email,desc,departamento,ciudad,barrio,):
 # driver.get("http://www.doctorsolucion.co/cita-presupuesto")
 # #lucky_button = driver.find_element_by_css_selector("[name=btnI]")
 # nameField = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtNome_I")
 # nameField.clear()
 # nameField.send_keys(name)
 
 # emailField = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtEmail_I")
 # emailField.clear()
 # emailField.send_keys(email)

 # phoneField = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtTelefoneCelular_I")
 # phoneField.clear()
 # phoneField.send_keys(phone)
 
 # phoneField2 = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtTelefone_I")
 # phoneField2.clear()
 # phoneField2.send_keys(phone2)
 
 
 # direccionField = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtEndereco_I")
 # direccionField.clear()
 # direccionField.send_keys()
 
 # selectDepartamento = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboEstado_I")
 # selectDepartamento.clear()
 # selectDepartamento.send_keys(departamento)
 
 
 # #selectCiudad = WebDriverWait(driver, secs).until(find,ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboCidade_I)
 
 # #selectCiudad = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboCidade_I")
 # selectCiudad.clear()
 # selectCiudad.send_keys(ciudad)
 
 # driver.implicitly_wait(30)
 
 # selectBarrio = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboBairro_I")
 # selectBarrio.clear()
 # selectBarrio.send_keys(barrio)
 
 # driver.implicitly_wait(30)
 
 # selectComo = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboMidia_I")
 # selectComo.clear()
 # selectComo.send_keys("Internet")
 
 # driver.implicitly_wait(15)
 
 # selectDonde = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_cboMidia_I")
 # selectDonde.clear()
 # selectDonde.send_keys("Email")
 
 # driver.implicitly_wait(15)
 
 # descripcionField=driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_txtMensagem_I")
 # descripcionFieldclear()
 # descripcionField.send_keys(desc)
 
 # driver.implicitly_wait(15)
 
 # submitBtn=driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucOrcamentoOnline_btnEnviar")
 # driver.get_screenshot_as_file("capturaDoctorAntesEnvio.png") 
 # submitBtn.click()

 # print("-------------")
 # print("-------------")


 # #lucky_button.click()
 # print(driver.title)
 # # capture the screen
 # driver.get_screenshot_as_file("capturaDoctorDespuesEnvio.png") 
 
 # def find(driver,id):
    # element = driver.find_elements_by_id(id)
    # if element:
        # return element
    # else:
        # return False
electricistas24Horas("Ricardo","3000000000","t.kavanagh@uniandes.edu.co","Necesito que arrglen a mi perro aaaaaaaaaaaaaaaaaaaaaa xp")
expertoYa("Jairo","3000000000","jularenas11@gmail.com","necesito un cerrajero ","cll 66#32-21",1,"10 Mayo 2018","20")
#doctorSolucion("Ricardo","3142352865","305717646","jularenas@gmail.com","envio de prueba","Bogotá","Bogotá","BOCHICA")