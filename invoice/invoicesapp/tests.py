from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2023-10-01', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_invoice(self):
        response = self.client.get(f'/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, 200)
