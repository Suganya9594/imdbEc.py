from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class IMDBAutomation:
    def __init__(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
       # Path to the uBlock Origin extension
        extension_path = "uBlock0_1.60.1b9.firefox.signed.xpi"

        # Add the extension after starting the session
        self.driver.install_addon(extension_path, temporary=True)


    def open_page(self, url):
        # Open the specified IMDb search page
        self.driver.get(url)
        self.driver.maximize_window()


    def click_accordion(self, xpath):
        # Click on the accordion
        accordion_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        accordion_label.click()
        def scroll_down(self):
        
        # Scroll down the page
         self.driver.execute_script("window.scrollTo(0, window.scrollY + 500);")  

    def enter_value(self, name, id_name):
        # Wait for the input field to be visible
        input_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, id_name))
        )
        
        # Click and focus on the input field
        input_field.click()
        self.driver.execute_script("arguments[0].focus();", input_field)
        self.driver.execute_script("arguments[0].value = '';", input_field)  # Clear existing value
        
        # Send the name and press Enter
        input_field.send_keys(name)
        input_field.send_keys(Keys.RETURN)

    def close(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    imdb_bot = IMDBAutomation()
    try:
        imdb_bot.open_page("https://www.imdb.com/search/name/")
        imdb_bot.click_accordion("//label[@role='button' and @aria-controls='accordion-item-nameTextAccordion']")
        imdb_bot.enter_value("Bruce Lee", "name-text-input")
        imdb_bot.click_accordion("//label[@role='button' and @aria-controls='accordion-item-birthdayAccordion']")
        imdb_bot.enter_value("11-27", "birthday-input")
        

    finally:
        imdb_bot.close()


