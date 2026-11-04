import json
import unittest
from unittest.mock import MagicMock, patch

from fellow_aiden import FellowAiden


def _response(payload, status_code=200):
    response = MagicMock()
    response.status_code = status_code
    response.content = json.dumps(payload).encode("utf-8")
    return response


class TestAuthLogging(unittest.TestCase):

    def test_login_does_not_log_tokens(self):
        login = _response({"accessToken": "secret-access", "refreshToken": "secret-refresh"})
        devices = _response([{"id": "brewer-1", "displayName": "Aiden"}])
        with patch.object(FellowAiden.SESSION, "post", return_value=login), \
                patch.object(FellowAiden.SESSION, "get", return_value=devices), \
                self.assertLogs(FellowAiden.NAME, level="DEBUG") as logs:
            aiden = FellowAiden("user@example.com", "hunter2")

        self.assertEqual(aiden._token, "secret-access")
        output = "\n".join(logs.output)
        for secret in ("secret-access", "secret-refresh", "hunter2"):
            self.assertNotIn(secret, output)


if __name__ == "__main__":
    unittest.main()
