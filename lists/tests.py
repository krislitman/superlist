from django.test import TestCase


class SmokeTest(TestCase):

    def test_bad_stuff(self):
        self.assertEqual(1 + 1, 100)
