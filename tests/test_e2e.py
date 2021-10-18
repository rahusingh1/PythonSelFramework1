from pageObjects.HomePage import HomePage
from utilities.BaseClass import baseClass

class TestOne(baseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        # homepage.shopitems().click()
        checkoutpage = homepage.shopitems()
        log.info("getting all the card titles")
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()

        # checkoutpage = CheckOutPage(self.driver)
        products = checkoutpage.getcardTitles()
        # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        # //div[@class='card h-100']/div/h4/a
        for product in products:
            productname = product.find_element_by_xpath("div/h4/a").text
            log.info(productname)
            if productname == "Blackberry":
                # add item to cart
                product.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a.btn-primary").click()
        #checkoutpage.clickprimary().click()

        # assets = self.driver.find_element_by_link_text("Blackberry").text
        assets = checkoutpage.clickelement().text
        assert assets == "Blackberry"

        # self.driver.find_element_by_css_selector("button.btn-success").click()
        confirmPage = checkoutpage.clicksuccess()

        log.info("Entering country name as ind")
        # self.driver.find_element_by_id("country").send_keys("ind")
        # confirmPage = ConfirmPage(self.driver)
        confirmPage.entrcountry().send_keys("ind")

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")  # after making the utility of explicit wait you use like this.

        # self.driver.find_element_by_link_text("India").click()
        confirmPage.selectindia().click()
        # self.driver.find_element_by_css_selector(".checkbox-primary").click()
        confirmPage.checked().click()
        # self.driver.find_element_by_css_selector("input[type='submit']").click()
        confirmPage.submitted().click()

        # successmsg = self.driver.find_element_by_css_selector("div[class*='alert-success']").text
        successmsg = confirmPage.successMessage().text
        print(successmsg)
        log.info("Text received from application is "+successmsg)
        assert "Success!" in successmsg

        self.driver.get_screenshot_as_file("screen.png")  # to get screenshot and save as file

        self.driver.close()
