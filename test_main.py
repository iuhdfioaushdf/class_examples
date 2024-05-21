from os import path
import unittest
from unittest import TestCase
from mock import Mock, mock_open
from mock import patch
import main

class TestMain(TestCase):
    def setUp(self):
        # self.csv_dict_reader_backup = main.csv.DictReader
        self.user_collection = main.init_user_collection()


    def tearDown(self):
        pass


    def test_init_user_collection(self):
        """main.py init_user_collection function - return"""
        good_data = main.users.UserCollection()
        self.assertIsInstance(good_data,main.users.UserCollection)


    def test_init_user_status_collection(self):
        """main.py init_user_status_collection function - return"""
        good_data = main.user_status.UserStatusCollection()
        self.assertIsInstance(good_data,main.user_status.UserStatusCollection)


    def test_load_user_pass(self):
        with patch('main.open',mock_open()):
            good_file = iter([{
            'USER_ID': 'epales_01',
            'EMAIL': 'epales@email.com',
            'NAME': 'eric',
            'LASTNAME': 'pales'
        },])
            user_collection = main.init_user_collection()
            main.csv.DictReader = Mock(return_value=good_file)
            self.assertTrue(main.load_users(user_collection,'some.csv'))


    def test_save_user_pass(self):

        open_mock = mock_open()

        with patch("main.open", open_mock, create=True):
            main.save_users(self.user_collection,filename='test.csv')
        
        open_mock.assert_called_with('test.csv', 'w')
        open_mock.return_value.write.assert_called_once_with(self.user_collection,filename='test.csv')


    # def test_save_user_pass(self):
    #     open_mock = mock_open()
    #     with patch('main.open',open_mock, create=True):
    #         good_data = iter([{
    #         'USER_ID': 'epales_01',
    #         'EMAIL': 'epales@email.com',
    #         'NAME': 'eric',
    #         'LASTNAME': 'pales'
    #     },])
    #         main.save_users(good_data, filename='test.csv')
    #         open_mock.assert_called_with('test.csv', 'w')
    #         open_mock.return_value.write.assert_called_once_with(good_data,filename='test.csv')



    def test_load_status_updates_pass(self):
        with patch('main.open',mock_open()):
            good_data = iter([{
            'STATUS_ID' : 'epales_001',
            'USER_ID': 'epales',
            'STATUS_TEXT': 'beautiful day today'
        },])

            status_collection = Mock(main.init_status_collection())
            main.csv.DictReader = Mock(return_value=good_data)
            self.assertTrue(main.load_status_updates(status_collection,'some_2.csv'))


    # def test_save_status_updates_pass(self):
    #     good_data = iter([{
    #         'STATUS_ID' : 'epales_001',
    #         'USER_ID': 'epales',
    #         'STATUS_TEXT': 'beautiful day today'
    #     },])
    #     status_collection = Mock(main.init_status_collection())
    #     main.csv.DictWriter = Mock(return_value=good_data)
    #     self.assertTrue(main.load_status_updates(status_collection,'some_2.csv'))


    def test_add_user_false(self):
        """main.py add_user function returns - false"""
        good_data = ('epales01','epales@email.com','epales','pales')
        user_id = good_data[0]
        email = good_data[1]
        user_name = good_data[2]
        user_last_name = good_data[3]

        user_collection = main.init_user_collection()
        user_collection.add_user(user_id, email, user_name, user_last_name)
        self.assertEqual(user_collection.add_user(user_id, email, user_name, user_last_name), False)


    def test_add_user_pass(self):
        """main.py add_user function - pass"""
        good_data = ('epales01','epales@email.com','epales','pales')
        user_id = good_data[0]
        email = good_data[1]
        user_name = good_data[2]
        user_last_name = good_data[3]

        user_collection = main.users.UserCollection()
        user_collection.add_user(user_id, email, user_name, user_last_name)
        self.assertEqual(main.init_user_collection().add_user(user_id, email, user_name, user_last_name), True)


    def test_modify_user_false(self):
        """main.py update_user function - false"""
        good_data = ('epales01','epales@email.com','epales','pales')
        user_id = good_data[0]
        email = good_data[1]
        user_name = good_data[2]
        user_last_name = good_data[3]
        
        bad_data = ('epales', 'epales_1@email.com', 'erik', 'payless')
        user_id_1 = bad_data[0]
        email_1 = bad_data[1]
        user_name_1 = bad_data[2]
        user_last_name_1 = bad_data[3]

        user_collection = main.users.UserCollection()
        user_collection.add_user(user_id, email, user_name, user_last_name)
        self.assertEqual(main.init_user_collection().modify_user(user_id_1, email_1, user_name_1, user_last_name_1), False)


    def test_modify_user_true(self):
        """main.py update_user function - true"""
        good_data = ('epales01','epales@email.com','epales','pales')
        user_id = good_data[0]
        email = good_data[1]
        user_name = good_data[2]
        user_last_name = good_data[3]

        updated_data = ('epales01', 'test@email.com', 'erick', 'payless')
        user_id_1 = updated_data[0]
        email_1 = updated_data[1]
        user_name_1 = updated_data[2]
        user_last_name_1 = updated_data[3]

        user_collection = main.users.UserCollection()
        user_collection.add_user(user_id, email, user_name, user_last_name)

        get_from_main = user_collection.modify_user(user_id_1, email_1, user_name_1, user_last_name_1)

        self.assertIs(get_from_main, True)


    def test_delete_user_pass(self):
        """main.py delete_user function - pass"""
        good_data = ('epales01','epales@email.com','epales','pales')
        user_id = good_data[0]
        email = good_data[1]
        user_name = good_data[2]
        user_last_name = good_data[3]

        user_collection = main.users.UserCollection()
        user_collection.add_user(user_id, email, user_name, user_last_name)

        get_from_main = user_collection.delete_user(user_id)

        self.assertIs(get_from_main, True)


    def test_delete_user_false(self):
        """main.py delete_user function - false"""
        good_data = ('epales01','epales@email.com','epales','pales')
        user_id = good_data[0]
        email = good_data[1]
        user_name = good_data[2]
        user_last_name = good_data[3]

        bad_data = 'epales'

        user_collection = main.users.UserCollection()
        user_collection.add_user(user_id, email, user_name, user_last_name)

        get_from_main = user_collection.delete_user(bad_data)

        self.assertFalse(get_from_main)


    def test_search_user_pass(self):
        """main.py search_user function - pass"""
        good_data = ('epales01','epales@email.com','epales','pales')
        user_id = good_data[0]
        email = good_data[1]
        user_name = good_data[2]
        user_last_name = good_data[3]

        user_collection = main.users.UserCollection()
        user_collection.add_user(user_id, email, user_name, user_last_name)

        get_from_main = user_collection.search_user(user_id)

        self.assertIs(get_from_main,user_collection.search_user(user_id))


    def test_search_user_none(self):
        """main.py search_user function - none"""
        good_data = ('epales01','epales@email.com','epales','pales')
        user_id = good_data[0]
        email = good_data[1]
        user_name = good_data[2]
        user_last_name = good_data[3]

        user_collection = main.users.UserCollection()
        user_collection.add_user(user_id, email, user_name, user_last_name)

        bad_data = 'orion'
        get_from_main = user_collection.search_user(bad_data)

        self.assertIsNotNone(get_from_main)


    def test_add_status_pass(self):
        """main.py add_status function - pass"""
        good_data = ('epales0001','epales@email.com','the sun is hot today')
        status_id = good_data[0]
        user_id = good_data[1]
        status_text = good_data[2]


        status_collection = main.user_status.UserStatusCollection()
        status_collection.add_status(status_id, user_id, status_text)
        self.assertEqual(main.init_status_collection().add_status(status_id, user_id, status_text),True)


    def test_add_status_false(self):
        """main.py add_status function - false"""
        good_data = ('epales0001','epales@email.com','the sun is hot today')
        status_id = good_data[0]
        user_id = good_data[1]
        status_text = good_data[2]


        status_collection = main.user_status.UserStatusCollection()
        status_collection.add_status(status_id, user_id, status_text)
        self.assertEqual(status_collection.add_status(status_id, user_id, status_text),False)


    def test_update_status_pass(self):
        """main.py update_status function - pass"""
        good_data = ('epales_001','epales','beautiful day today')
        status_id = good_data[0]
        user_id = good_data[1]
        status_text = good_data[2]

        updated_data = ('epales_001', 'epales', 'summer is starting early!')
        status_id_1 = updated_data[0]
        user_id_1 = updated_data[1]
        status_text_1 = updated_data[2]

        status_collection = main.user_status.UserStatusCollection()
        status_collection.add_status(status_id, user_id, status_text)

        get_from_main = status_collection.modify_status(status_id_1, user_id_1, status_text_1)

        self.assertIs(get_from_main, True)


    def test_modify_status_false(self):
        """main.py update_status function - false"""
        good_data = ('epales0001','epales@email.com','the sun is hot today')
        status_id = good_data[0]
        user_id = good_data[1]
        status_text = good_data[2]
        
        bad_data = ('epales', 'epales@email.com', 'the sun is hot today')
        status_id_1 = bad_data[0]
        user_id_1 = bad_data[1]
        status_text_1 = bad_data[2]

        status_collection = main.user_status.UserStatusCollection()
        status_collection.add_status(status_id, user_id, status_text)
        self.assertEqual(main.init_status_collection().modify_status(status_id_1, user_id_1, status_text_1), False)


    def test_delete_status_pass(self):
        """main.py delete_status function - pass"""
        good_data = ('epales0001','epales@email.com','the sun is hot today')
        status_id = good_data[0]
        user_id = good_data[1]
        status_text = good_data[2]

        status_collection = main.user_status.UserStatusCollection()
        status_collection.add_status(status_id, user_id, status_text)

        get_from_main = status_collection.delete_status(status_id)
        self.assertIs(get_from_main, True)


    def test_delete_status_false(self):
        """main.py delete_status function - false"""
        good_data = ('epales0001','epales@email.com','the sun is hot today')
        status_id = good_data[0]
        user_id = good_data[1]
        status_text = good_data[2]

        bad_data = 'epales0002'

        status_collection = main.user_status.UserStatusCollection()
        status_collection.add_status(status_id, user_id, status_text)

        get_from_main = status_collection.delete_status(bad_data)
        self.assertFalse(get_from_main)


    def test_search_status_pass(self):
        """main.py search_status function - pass"""
        good_data = ('epales0001','epales@email.com','the sun is hot today')
        status_id = good_data[0]
        user_id = good_data[1]
        status_text = good_data[2]

        status_collection = main.user_status.UserStatusCollection()
        status_collection.add_status(status_id, user_id, status_text)

        get_from_main = status_collection.search_status(status_id)

        self.assertIs(get_from_main,status_collection.search_status(status_id))


    def test_search_status_none(self):
        """main.py search_user function - none"""
        good_data = ('epales0001','epales@email.com','the sun is hot today')
        status_id = good_data[0]
        user_id = good_data[1]
        status_text = good_data[2]

        status_collection = main.user_status.UserStatusCollection()
        status_collection.add_status(status_id, user_id, status_text)

        bad_data = 'epales0002'
        get_from_main = status_collection.search_status(bad_data)

        self.assertIsNotNone(get_from_main)


if __name__ == '__main__':
    
    unittest.main(verbosity=2)