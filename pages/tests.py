from django.test import SimpleTestCase, TestCase

from django.urls import reverse

# Create your tests here.


class HomePgTests(SimpleTestCase):

    def test_homepg_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepg_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepg_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepg_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Home Page')


class AboutPgTests(TestCase):

    def test_about_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_url_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'about.html')

    def test_about_html_used(self):
        response = self.client.get('/about/')
        self.assertContains(response, 'About')
