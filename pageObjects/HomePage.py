from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR, "[name='email']")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CLASS_NAME, "btn-success")
    alert = (By.CLASS_NAME, "alert-success")

    def shopitems(self):
        # return self.driver.find_element(*HomePage.shop)  # perform same action shown below
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver) # here create object of next page
        return checkoutPage # return object of next page.
        #driver.find_element_by_css_selector("a[href*='shop']")

    def fullname(self):
        return self.driver.find_element(*HomePage.name)

    def Email(self):
        return self.driver.find_element(*HomePage.email)

    def Checkbox(self):
        return self.driver.find_element(*HomePage.check)

    def GenderOptions(self):
        return self.driver.find_element(*HomePage.gender)

    def Submit(self):
        return self.driver.find_element(*HomePage.submit)

    def Alert(self):
        return self.driver.find_element(*HomePage.alert)