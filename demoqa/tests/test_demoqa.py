import pytest
import unittest

from selenium import webdriver

from demoqa.src.demoqa import demoqaPageObject

# Based on my own sample  https://github.com/revfran/toxPytest_Sample/blob/master/tests/test_sample.py
class demoqaTest(unittest.TestCase):
    

    def setUp(self):
        desiredCapabilities={"browserName":"chrome"}
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities = desiredCapabilities)
        self.page = demoqaPageObject()

    def tearDown(self):
        self.driver.quit()

    def test_self(self):
        self.driver.get("chrome://settings/help")
        title = self.driver.title
        assert len(title) > 0

    def test_login(self):
        self.driver.get(self.page.baseUrl)
        title = self.driver.title
        print(f"Current title: {title}")
        assert self.page.isTitleExpected(title)

if __name__ == "__main__":
    unittest.main()

