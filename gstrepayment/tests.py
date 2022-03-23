from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse
from users.models import CustomUser
from .models import Entry, OtherTaxes

# Create your tests here.
class TestsHome(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class TestUserType(TestCase):

    def setUp(self):

        # Tax Payer
        self.taxPayer = CustomUser.objects.create_user(
            username = 'testtaxpayer',
            gst_num = '22FXSP5355ML123',
            user_type = 'TP',
            password = 'pass@123',
        )

        # Tax Accountant
        self.taxAccountant = CustomUser.objects.create_user(
            username = 'testtaxaccountant',
            gst_num = '20FXSP5355ML123',
            user_type = 'TA',
            password = 'pass@123',
        )

        # Creating Sale Entry by Tax Payer
        self.saleEntry = Entry.objects.create(
            seller = self.taxPayer,
            sale_item = "testitem",
            buyer = '21FXSP55ML55123',
            amount = 100000,
        )

        # Creating Other Tax entry by Accountant
        self.otherTaxEntry = OtherTaxes.objects.create(
            accountant = self.taxAccountant,
            tax_name = "testTax",
            tax_payer = self.taxPayer,
            amount = 100000,
            due_date = '2022-04-23'
        )

    def test_entry_content(self):
        self.assertEqual(f'{self.saleEntry.seller}', 'testtaxpayer')

    def test_other_tax_entry(self):
        self.assertEqual(f'{self.otherTaxEntry.accountant}', 'testtaxaccountant'),
        self.assertEqual(f'{self.otherTaxEntry.tax_payer}', f'{self.taxPayer}')


class TestTemplates(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user("testuser", "test@email.com", "pass@123")

        self.entry = Entry.objects.create(
            seller = self.user,
            sale_item = "testitem",
            buyer = 'testgstin',
            amount = 100,
        )

    def test_addEntry_template(self):
        response = self.client.get(reverse('add_entry'))
        # Trying with out login
        self.assertNotEqual(response.status_code, 200)

        # Login and asking the template
        self.client.login(username="testuser", password="pass@123")
        response = self.client.get(reverse('add_entry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gstrepayment/add_entry.html')

    def test_DeleteEntry_template(self):
        self.client.login(username="testuser", password="pass@123")
        response = self.client.get(reverse('delete_entry', args=(self.entry.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gstrepayment/delete_entry.html')



        