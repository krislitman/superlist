from django.test import TestCase
from django.urls import resolve
from lists.views import home


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        path = resolve('/')
        self.assertEqual(path.func, home)
