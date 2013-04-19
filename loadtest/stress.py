import json
import random
from funkload.FunkLoadTestCase import FunkLoadTestCase
from funkload.utils import Data


class StressTest(FunkLoadTestCase):

    def setUp(self):
        self.server_url = self.conf_get("main", "url")
        if not self.server_url.endswith("/"):
            self.server_url += "/"

    def test_simple(self):
        self.setOkCodes([200])
        response = self.get(self.server_url + "/")
        self.assertTrue(response.body != '')

