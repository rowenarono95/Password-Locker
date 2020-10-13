import unittest 
from user_details import User 
from user_details import Credentials

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Rowena", "Rono", "1234")
        
    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Rowena")
        self.assertEqual(self.new_user.second_name, "Rono")
        self.assertEqual(self.new_user.password, "1234")

        '''
        test_init_details user can add more than credential that is first name,secondname and password
        '''
    def test_save(self):
        self.new_user.signup()
        self.assertEqual(len(User.user),1)

        '''
        test_save_details test case to test if the details are saved into
         the user list
        '''

    def test_sign_up(self):
        self.new_user.signup()
        self.assertEqual(len(User.user),1)

    def test_login(self):         
        self.assertTrue(self.new_user.first_name, 'Rowena')
        self.assertTrue(self.new_user.second_name, 'Rono') 
        self.assertTrue(self.new_user.password, '1234')

    def test_login(self):
        self.new_user.login()
        self.assertEqual(len(User.user),1)

        '''
        test_login if user can add more than one login details
        '''

    def test_delete(self):
        self.new_user.delete_cred()
        self.assertEqual(len(Credentials.user),1)

        '''
        test_delete test to check is user can delete details

        '''

    def test_view(self):
        self.new_user.view()
        self.assertEqual(len(User.user),1)

        '''
        test_view_details testvto check if the user is given an option for viewing credetials

        '''


if __name__ == '__main__':
    unittest.main()

      