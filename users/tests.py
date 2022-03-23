from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse

class UserTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username = 'testusername',
            user_type = 'TP',
            gst_num = "123456789ABCDE", 
            password = 'pass@123',           
        )

    def test_signup_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')
    
    def test_edit_view_uses_correct_template(self):
        response = self.client.get(reverse('edit_user', args=(self.user.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/edit_user.html')
