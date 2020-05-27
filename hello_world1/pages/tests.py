from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def tets_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code,200)

    def tets_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code,200)
