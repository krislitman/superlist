from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class UserVisitsPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_get_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Habits', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
