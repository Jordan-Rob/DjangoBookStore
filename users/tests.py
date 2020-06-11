from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='jay',
            email='jay@jay.dev',
            password='test@jay',
        )

        self.assertEqual(user.username, 'jay')
        self.assertEqual(user.email, 'jay@jay.dev')

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@admin.co',
            password='admin'
        )

        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@admin.co')

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)


class SignUpTests(TestCase):

    def test_signup(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_template_used(self):
        response = self.client.get('/signup/')
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_html(self):
        response = self.client.get('/signup/')
        self.assertContains(response, 'Sign Up for an Account')


class SignUpFormTests(Testcase):
    def test_user_signup(self):
        new_user = get_user_model().objects.create_user(
            username='kolio',
            email='kolio@kolio.com',
            password='kolio'
        )

        self.assertEqual(new_user.username, 'kolio')
        self.assertEqual(new_user.email, 'kolio@kolio.com')
        self.assertEqual(get_user_model().objects.all().count(), 1)
