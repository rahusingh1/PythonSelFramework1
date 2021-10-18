from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_id("country")
    country = (By.ID, "country")

    # self.driver.find_element_by_link_text("India")
    india = (By.LINK_TEXT, "India")

    # self.driver.find_element_by_css_selector(".checkbox-primary").click()
    check = (By.CSS_SELECTOR, ".checkbox-primary")

    # self.driver.find_element_by_css_selector("input[type='submit']").click()
    submit = (By.CSS_SELECTOR, "input[type='submit']")

    # self.driver.find_element_by_css_selector("div[class*='alert-success']")
    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def entrcountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectindia(self):
        return self.driver.find_element(*ConfirmPage.india)

    def checked(self):
        return self.driver.find_element(*ConfirmPage.check)

    def submitted(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.alert)