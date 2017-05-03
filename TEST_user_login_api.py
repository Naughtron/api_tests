import requests
import unittest

class test_invalid_POST_login(unittest.TestCase):
    def setUp(self):
        self.payload = {'username':'testuser', 'password':'password'}
        self.url = 'https://www.hackthissite.org'

    
    def test_POST_invalid_login(self):
        payload = self.payload
        url = self.url + '/user/login'
        # make request: 
        POST_req = requests.post(url, data=payload)
        # assert response code 
        self.assertEqual(POST_req.status_code, 200)
        
    def test_GET_invalid_URL(self):
        url = self.url + '/jhdskjalhsasdfhadskh'
        # make request: 
        GET_req = requests.get(url)
        # assert response code 
        self.assertEqual(GET_req.status_code, 404)
        
    def test_SQL_Inj_01(self):
        url = self.url + '/missions/realistic/4/addemail.php'
        payload = {'email': "'or1=1--"}
        headers = {'Referer': 'https://www.hackthissite.org/missions/realistic/4/'}
        expected_error = "Error inserting into table \"email\"! Email not valid! Please contact an administrator of Fischer's"
        # make request:
        POST_req = requests.post(url, data=payload, headers=headers)
        # assert correct error is returned
        self.assertEqual(expected_error, POST_req.content)
         
if __name__ == '__main__':
    unittest.main()
    
            