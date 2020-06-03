from django.test import TestCase
from django.contrib.auth import get_user_model
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
