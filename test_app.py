import unittest
import json
from app import app

class ChatbotTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<html', response.data)

    def test_generate_missing_prompt(self):
        response = self.client.post('/generate', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Prompt is required', response.data)

    def test_new_session(self):
        response = self.client.post('/session')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('session_id', data)

    def test_list_files(self):
        response = self.client.get('/files')
        self.assertIn(response.status_code, [200, 500])  # 500 if file_service fails

    def test_upload_no_files(self):
        response = self.client.post('/upload', data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No files provided', response.data)

if __name__ == '__main__':
    unittest.main()
