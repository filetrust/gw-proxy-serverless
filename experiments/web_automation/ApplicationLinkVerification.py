import unittest
from selenium import webdriver


class LinkVerifictionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
        cls.driver.maximize_window()

    def setUp(self):

        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)


    def test_TechnologyPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[1]/ul/li[1]/a").click()
        technologyPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/section/div/div/div[1]/h2")
        print(technologyPageLabel.text)
        self.assertEqual(technologyPageLabel.text, "Introducing d-FIRST™", "Technology Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/technology/", "Technology Page not Opened")

    def test_SolutionsPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[1]/ul/li[2]/a").click()
        solutionPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/div[1]/section/div/div/div[1]/h2")
        print(solutionPageLabel.text)
        self.assertEqual(solutionPageLabel.text, "Solutions", "Solutions Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/solutions/", "Solutions Page not Opened")

    def test_ResourcesPage_Pass(self):
        self.driver.get("https://glasswallsolutions.com/")
        headerTitle = self.driver.title
        print(headerTitle)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div[2]/nav/div[1]/ul/li[3]/a").click()
        resourcesPageLabel = self.driver.find_element_by_xpath("//*[@id='main']/div/section/div/div/div[1]/h2")
        print(resourcesPageLabel.text)
        self.assertEqual(resourcesPageLabel.text, "CEO BLOG", "Resources Page not Opened")
        self.assertEqual(self.driver.current_url, "https://glasswallsolutions.com/resources/", "Resources Page not Opened")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()