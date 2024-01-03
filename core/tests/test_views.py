from django.test  import TestCase
from ..models import User
from django.urls import reverse
from django.db import IntegrityError

class ProfileViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create(username="testuser",email="abc@gmail.com")
        test_user.set_password("abcdefgh")
        test_user.save()
    

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('profile'))
        self.assertTrue(response.url.startswith('/accounts/login/'))
    
    def test_logged_in(self):
        self.client.login(username="testuser",password="abcdefgh")
        response = self.client.get(reverse('profile'))

        self.assertEqual(str(response.context['user']),'testuser') # Check to see logged-in user


        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'core/profile.html')

class RegisterViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create(username="testuser",email="abc@gmail.com")
        test_user.set_password("abcdefgh")
        test_user.save()
    
    def test_register_redirect(self):
        post_body = {
            "Username":"testuser1",
            "Email":"hcd@gmail.com",
            "Password":"abcdefgh",
            "ConfirmPassword":"abcdefgh"
        }
        response = self.client.post(reverse('register'),post_body)
        self.assertTrue(response.url.startswith("/accounts/login/"))
    