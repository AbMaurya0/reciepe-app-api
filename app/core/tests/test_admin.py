"""
Test for the Django admin modifications.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self) :
        """Cretse user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'user@example.com',
            password = 'testpass123',
            name = 'Abhishek'
        )

    def test_users_list(abhi):
        """Test that users are listed on page"""
        url = reverse('admin:core_user_changelist')
        res = abhi.client.get(url)

        abhi.assertContains(res, abhi.user.name)
        abhi.assertContains(res, abhi.user.email)

    def test_edit_user_page(self):
        """Test that edit the user page works"""
        url = reverse('admin:core_user_change',args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the Create user page words"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)
