from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = self.client.get('/')
        self.assertTemplateUsed(found, 'home.html')

    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())

    def test_home_page_returns_correct_content(self):
        response = self.client.get('/')

        content = response.content.decode('utf8')
        self.assertTrue(content.startswith('<html>'))
        self.assertIn('<title>To-Do Lists</title>', content)
        self.assertTrue(content.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')
