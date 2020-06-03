from django.test import SimpleTestCase

from django.urls import reverse

# Create your tests here.


class HomePgTests(SimpleTestCase):

    def test_homepg_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepg_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
