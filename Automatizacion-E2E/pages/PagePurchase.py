from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time
import unittest

class PurchasePg(unittest.TestCase):        
    def get_driver(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def navigate(self):
        self.driver.get('https://www.demoblaze.com')

    def add_to_cart(self,producto):
        #ESPERAR HASTA QUE SE LOCALICE AL PRIMER PRODUCTO
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,f"//a[contains(text(),'{producto}')]")))

        #PRIMER PRODUCTO
        producto_1 = self.driver.find_element(By.XPATH,f"//a[contains(text(),'{producto}')]")
        producto_1.click()

        #ESPERAR  HASTA QUE APAREZCA Y PUEDA SER CLICKEABLE 
        wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Add to cart')]")))
        btn_add_to_cart = self.driver.find_element(By.XPATH,"//a[contains(text(),'Add to cart')]")
        btn_add_to_cart.click()
        time.sleep(3)        
        try:
            alerta = self.driver.switch_to.alert
            alerta.accept()  # alerta.dismiss() si deseas cancelar la alerta
        except NoAlertPresentException:
            print("No se encontró ninguna alerta")

    def go_to_cart(self):
        #ESPERAR HASTA QUE SE LOCALICE EL LINK DEL CARRITO
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID,'cartur')))
        #PRIMER PRODUCTO
        link_cart = self.driver.find_element(By.ID,'cartur')
        link_cart.click()
        time.sleep(4)

    def go_to_home(self):
        link_home = self.driver.find_element(By.XPATH,"//a[contains(text(),'Home')]")
        link_home.click()

    def complete_form_checkout(self):
        #Seleccionar boton place order para abrir el checkout
        wait = WebDriverWait(self.driver, 10)
        
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Place Order')]")))
        btn_place_order = self.driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]")
        self.driver.execute_script("arguments[0].click();", btn_place_order)


        #completar formulario
        wait.until(EC.presence_of_element_located((By.ID,'name')))
        name = self.driver.find_element(By.ID,'name')
        name.send_keys('Greis Loyaga')

        country = self.driver.find_element(By.ID,'country')
        country.send_keys('Peru')

        city = self.driver.find_element(By.ID,'city')
        city.send_keys('Trujillo')

        credit_card = self.driver.find_element(By.ID,'card')
        credit_card.send_keys('4919148107859067')

        month = self.driver.find_element(By.ID,'month')
        month.send_keys('03')
        
        year = self.driver.find_element(By.ID,'year')
        year.send_keys('2025')
        
    def purchase(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Purchase')]")))
        btn_purchase = self.driver.find_element(By.XPATH,"//button[contains(text(), 'Purchase')]")
        btn_purchase.click()

    def validate_success_purchase(self):
        message_success_purchase = self.driver.find_element(By.XPATH,"//h2[contains(text(),'Thank you for your purchase')]")
        self.assertEqual(message_success_purchase.text, "Thank you for your purchase!", 'Error, no se completó la compra')

