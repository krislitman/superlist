from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = self.client.get('/')
        self.assertTemplateUsed(found, 'home.html')

    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_returns_correct_content(self):
        response = self.client.get('/')

        content = response.content.decode('utf8')
        self.assertTrue(content.startswith('<html>'))
        self.assertIn('<title>To-Do Lists</title>', content)
        self.assertTrue(content.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(text='Guitar')
        Item.objects.create(text='Drums')

        response = self.client.get('/')

        self.assertIn('Guitar', response.content.decode())
        self.assertIn('Drums', response.content.decode())


class ItemModelTestCase(TestCase):

    def test_saving_and_retrieving_items(self):
        first = Item()
        first.text = 'This is the first item'
        first.save()

        second = Item()
        second.text = 'This is the second item'
        second.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'This is the first item')
        self.assertEqual(second_saved_item.text, 'This is the second item')

    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
