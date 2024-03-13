from pages.PagePurchase import PurchasePg
import unittest
import time
from selenium import webdriver
import pytest

class PurchaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.purchase_page = PurchasePg()
        cls.driver = cls.purchase_page.get_driver()
        cls.driver.maximize_window()
    
    def test_01_add_product_to_cart(self):
        self.purchase_page.navigate()
        self.purchase_page.add_to_cart("Samsung galaxy s6")
        self.purchase_page.go_to_home()
        self.purchase_page.add_to_cart("Nokia lumia 1520")
        
    
    def test_02_go_to_cart(self):
        self.purchase_page.go_to_cart()    
    
    def test_03_complete_to_checkout_form(self):
        self.purchase_page.complete_form_checkout()
   
    def test_04_purchase(self):    
        time.sleep(5)
        self.purchase_page.purchase() 
        self.purchase_page.validate_success_purchase()
        
    @classmethod
    def tearDownClass(cls) :
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()