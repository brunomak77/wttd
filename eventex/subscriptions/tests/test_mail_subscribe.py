from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Bruno Makhohl',
                    cpf='12345678901',
                    email='brunomakhl@hotmail.com',
                    phone='11-981934970')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'brunomakhl@hotmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['brunomakhl@hotmail.com', 'brunomakhl@hotmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Bruno Makhohl',
                    '12345678901',
                    'brunomakhl@hotmail.com',
                    '11-981934970']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)