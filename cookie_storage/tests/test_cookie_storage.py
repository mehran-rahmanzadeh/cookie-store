from django.test import TestCase

from cookie_storage.helpers import SessionHelper
from cookie_storage.tests.doubles import RequestDouble, DataDouble, SessionDouble


class TestCookieStorage(TestCase):
    def test_set_data_to_session(self):
        """test set data to session"""
        session = SessionDouble()
        request = RequestDouble(session)
        session_helper = SessionHelper(request)
        instance = DataDouble('test_value')
        session_helper.set(instance)
        self.assertEqual(request.session[f'{instance.__class__.__module__}.{instance.__class__.__name__}'], instance)

    def test_get_data_from_session(self):
        """test get data from session"""
        session = SessionDouble()
        request = RequestDouble(session)
        session_helper = SessionHelper(request)
        instance = DataDouble('test_value')
        request.session[f'{instance.__class__.__module__}.{instance.__class__.__name__}'] = instance
        self.assertEqual(session_helper.get(instance.__class__), instance)

    def test_delete_data_from_session(self):
        """test delete data from session"""
        session = SessionDouble()
        request = RequestDouble(session)
        session_helper = SessionHelper(request)
        instance = DataDouble('test_value')
        request.session[f'{instance.__class__.__module__}.{instance.__class__.__name__}'] = instance
        session_helper.delete(instance.__class__)
        self.assertNotIn(f'{instance.__class__.__module__}.{instance.__class__.__name__}', request.session)

    def test_clear_session(self):
        """test clear session"""
        session = SessionDouble()
        request = RequestDouble(session)
        session_helper = SessionHelper(request)
        instance = DataDouble('test_value')
        request.session[f'{instance.__class__.__module__}.{instance.__class__.__name__}'] = instance
        session_helper.clear()
        self.assertNotIn(f'{instance.__class__.__module__}.{instance.__class__.__name__}', request.session)
