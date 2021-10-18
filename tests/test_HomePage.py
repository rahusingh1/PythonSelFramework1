import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import baseClass


class TestHomePage(baseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["name"])
        homepage.fullname().send_keys(getData["name"])
        homepage.Email().send_keys(getData["email"])
        homepage.Checkbox().click()
        self.selectOptionByText(homepage.GenderOptions(), getData["gender"])
        homepage.Submit().click()
        alertText = homepage.Alert().text

        assert ("Success!" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
