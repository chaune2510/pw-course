from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class clickandtype():
    def test(self):
        baseURL="http://formy-project.herokuapp.com/form"
        driver = webdriver.Chrome(executable_path="C:\\python\\browsers\\chromedriver.exe")
        #maximize windows
        driver.maximize_window()
        #open URL
        driver.get(baseURL)
        driver.implicitly_wait(5)
        #type to first name
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys("Tam")
        #type to last name
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys("Tran")

        #type to job title
        driver.find_element_by_id("job-title").clear()
        driver.find_element_by_id("job-title").send_keys("QC")
        #click radio button
        driver.find_element_by_id("radio-button-2").click()
        #click check box
        driver.find_element_by_id("checkbox-1").click()
        #select dropdown
        selectdropdown = driver.find_element_by_id("select-menu")
        sel = Select(selectdropdown)
        sel.select_by_visible_text("5-9")
        #quit driver
        time.sleep(5)
        driver.quit()

ch = clickandtype()
ch.test()