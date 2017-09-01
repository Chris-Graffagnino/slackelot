import pytest
import mock

from slackelot.slackelot import SlackNotificationError, send_message


def test_send_message_success():
    """Returns True if response.status_code == 200"""
    with mock.patch('slackelot.slackelot.requests.post', return_value=mock.Mock(**{'status_code': 200})) as mock_response:
        webhook = 'https://hooks.slack.com/services/'
        assert send_message('foo', webhook) == True


def test_send_message_raises_error_bad_request():
    """Raises SlackNotificationError if response.status_code not 200"""
    with mock.patch('slackelot.slackelot.requests.post', return_value=mock.Mock(**{'status_code': 400})) as mock_response:
        with pytest.raises(SlackNotificationError) as error:
            webhook = 'https://hooks.slack.com/services/'
            send_message('foo', webhook)
        assert 'Slack notification failed' in str(error.value)


def test_send_message_raises_error_bad_webhook():
    """Raises SlackNotificationError if webhook_url malformed"""
    with mock.patch('slackelot.slackelot.requests.post', return_value=mock.Mock(**{'status_code': 200})) as mock_response:
        with pytest.raises(SlackNotificationError) as error:
            webhook = 'https://notthehookwerelookingfor.com'
            send_message('foo', webhook)
        assert 'webhook_url is not in the correct format' in str(error.value)
