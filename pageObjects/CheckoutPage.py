from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    primaryButton = (By.CSS_SELECTOR, "a.btn-primary")
    # self.driver.find_element_by_link_text("Blackberry")
    clicklink = (By.LINK_TEXT, "Blackberry")
    # self.driver.find_element_by_css_selector("button.btn-success")
    successButton = (By.CSS_SELECTOR, "button.btn-success")

    def getcardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def clickprimary(self):
        return self.driver.find_elements(*CheckOutPage.primaryButton)

    def clickelement(self):
        return self.driver.find_element(*CheckOutPage.clicklink)

    def clicksuccess(self):
        # return self.driver.find_element(*CheckOutPage.successButton)
        self.driver.find_element(*CheckOutPage.successButton).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
