import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_successful_login(self):
        response = self.app.post('/', data=dict(username='test', password='test'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, test!', response.data)

    def test_unsuccessful_login(self):
        response = self.app.post('/', data=dict(username='wrong', password='wrong'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Welcome, test!', response.data)

    def test_logout(self):
        response = self.app.post('/dashboard/test', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Welcome, test!', response.data)

if __name__ == '__main__':
    unittest.main()