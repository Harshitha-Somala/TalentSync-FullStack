import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'  # Update with your Flask app URL

    def test_get_job_listings(self):
        response = requests.get(f'{self.base_url}/job_listings')
        self.assertEqual(response.status_code, 200)
        self.assertIn('job_listings', response.json())

    def test_get_feedback(self):
        response = requests.get(f'{self.base_url}/feedback')
        self.assertEqual(response.status_code, 200)
        self.assertIn('feedback', response.json())

    def test_add_feedback(self):
        # Test adding feedback
        feedback_data = {"feedback_type" : "employer",
                         "message" : "I like the Website.",
                        "job_id" : 8,
                        "rating" : 4,
                        "user_id" : 6}
        response = requests.post(f'{self.base_url}/add_feedback', json=feedback_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

if __name__ == '__main__':
    unittest.main()
