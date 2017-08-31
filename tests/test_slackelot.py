import pytest
import mock

from slackelot.slackelot import SlackNotificationError, send_slack_message


def test_send_slack_message_success():
    with mock.patch('slackelot.slackelot.requests.post', return_value=mock.Mock(**{'status_code': 200})) as mock_response:
        type(mock_response).status_code = 200
        webhook = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
        assert send_slack_message('foo', webhook) == True


def test_send_slack_message_raises_slack_notification_error():
    pass


def test_send_slack_message_sleeps():
    pass
