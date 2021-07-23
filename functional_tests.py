from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time


class UserVisitsPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_get_it_later(self):
        # ? User visits the homepage
        self.browser.get('http://localhost:8000')

        # ? User notices the page title and header mention to-do lists
        self.assertIn('To-Do Lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # ? User is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # ? User types "Buy a new computer" into a text box
        inputbox.send_keys('Buy a new computer')

        # ? When user hits enter, the page updates, and now the page lists
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # ? "1: Buy a new computer" as an item in a to-do list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy a new computer' for row in rows),
            "New to-do item did not appear in table"
        )

        # ? There is still a text box inviting user to add another item.
        self.fail('Test isnt done')


if __name__ == '__main__':
    unittest.main()
