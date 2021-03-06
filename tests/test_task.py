from service.app import app
from service.common.utils.tests import responses

import unittest


class TaskTestCase(unittest.TestCase):

    def setUp(self):
        """
        Setup the application.
        :return: None
        """
        self.app = app.test_client()

    def tearDown(self):
        """
        Teardown the application.
        :return: None
        """
        pass

    def test_task_get(self):
        """
        Test the REST interface 'GET /task'
        :return:
        """
        rv = self.app.get("/task")
        self.assertEqual(200, rv.status_code, "HTTP status code mismatch")

        expected_1 = dict(status="OK")
        self.assertTrue(responses.match_data(rv, expected_1), "JSON mismatch")


if __name__ == "__main__":
    unittest.main()