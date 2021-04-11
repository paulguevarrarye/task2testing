import task2_app
from task2_app import app
import unittest
import json

class MyTestCase(unittest.TestCase):
    def test_response1(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_response(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_response_circle(self):
        tester = app.test_client(self)
        response = tester.get('/getcircle')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_response_square(self):
        tester = app.test_client(self)
        response = tester.get('/getsquare')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        print(response.content_type)
        self.assertEqual(response.content_type, 'application/json')

    def test_content_data(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        self.assertTrue(b'shape' in response.data)


    def test_content_length(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        temp = json.loads(response.data)['measurements']
        self.assertGreater(len(temp),0,msg='Not Populated')

    def testing_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertTrue(b'Hello' in response.data)

    def testing_calculate_circle(self):
        tester = app.test_client(self)
        response = tester.get('/getcircle')
        self.assertTrue(b'circumference' in response.data)

    def testing_calculate_square(self):
        tester = app.test_client(self)
        response = tester.get('/getsquare')
        self.assertTrue(b'perimeter' in response.data)

    def test_input(self):
        input = task2_app.getinput()
        self.assertGreater(input,0, msg='Negative')

    def test_calculate_circle(self):
        measurement, answer = task2_app.calculate_circle()
        self.assertGreater(answer, 0, msg='Negative')

    def test_calculate_square(self):
        measurement, answer = task2_app.calculate_square()
        self.assertGreater(answer, 0, msg='Negative')

if __name__ == '__main__':
    unittest.main()
