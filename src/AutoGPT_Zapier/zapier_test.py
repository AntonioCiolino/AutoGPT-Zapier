"""
Test class for Zapier integration
"""
import os
import unittest
import requests

from .zapier import call_webhook


class TestAutoGPT_Zapier(unittest.TestCase):
    """
    This is the plugin test class for Zapier Webhooks for Auto-GPT
    """

    def setUp(self):
        os.environ["ZAPIER_WEBHOOK_ENDPOINT"] = "<YOUR ENDPOINT HERE>"
        self.title = "title"
        self.content = "this is content"
        self.summary= "user testing summary"

    def tearDown(self):
        os.environ.pop("ZAPIER_WEBHOOK_ENDPOINT", None)

    def test_call_webhook(self):
        try:
            output = call_webhook(
                title=self.title,
                summary=self.summary,
                content=self.content,
            )
            self.assertEqual(output.status_code, 200)
        except requests.exceptions.HTTPError as e:
            self.assertEqual(e.response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
