import unittest
from app import app


class ConvertCurrencyTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_convert_currency(self):
        response = self.app.get('/api/rates?from=USD&to=RUB&value=1')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)

    def test_invalid_currency(self):
        response = self.app.get('/api/rates?from=USD&to=XYZ&value=1')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('error', data)


if __name__ == '__main__':
    unittest.main()
