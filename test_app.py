import json
import unittest
from app import app

class TestApp(unittest.TestCase):

    def test_check_integer_high(self):
        with app.test_client() as client:
            payload = {"integer": 101}
            response = client.post('/check_integer', json=payload)
            data = json.loads(response.data)
            self.assertEqual(data["result"], "high")

    def test_check_integer_low(self):
        with app.test_client() as client:
            payload = {"integer": 99}
            response = client.post('/check_integer', json=payload)
            data = json.loads(response.data)
            self.assertEqual(data["result"], "low")

    def test_check_integer_invalid(self):
        with app.test_client() as client:
            payload = {"string": "invalid"}
            response = client.post('/check_integer', json=payload)
            data = json.loads(response.data)
            self.assertEqual(data["error"], "Invalid input")

if __name__ == '__main__':
    unittest.main()
