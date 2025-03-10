from selenium.webdriver.common.by import By

class findElements():

    def __init__(self,driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "tagname":
            return By.TAG_NAME
        else:
            print("Locator type " + locatorType + "not correct/supported")
        return False

    def getElement(self,locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element found!")
        except:
            print("Element not found!")
        return element

    def isElementPresent(self,locator, byType):
        try:
            element = self.driver.find_element(byType,locator)
            if element is not None:
                print("Element found!")
                return True
            else:
                print("Element not found!")
                return False
        except:
            print("Element not found!")
            return False

    def elementPresenceCheck(self,locator, byType):
        try:
            elementList = self.driver.find_elements(byType,locator)
            if len(elementList) > 0:
                print("Element found!")
                return True
            else:
                print("Element not found!")
                return False
        except:
            print("Element not found!")
            return False