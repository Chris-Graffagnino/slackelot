import time
import requests


class SlackNotificationError(Exception):
    pass


def send_slack_message(message, webhook_url, pretext=None, title=None):
    """ Send slack message using webhooks

    Args:
        message (string)
        webhook_url (string), 'https://hooks.slack.com/services/{team id}/{bot or channel id}/{auth token}'
        pretext (string)
        title (string)
    """

    payload = {
        'attachments': [
            {
                'pretext': pretext,
                'title': title,
                'text': message,
                'mrkdwn_in': ['text', 'pretext']
            }
        ],
        'link_names': '1',
        'as_user': True
    }

    for i in range(10):
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            return True
        else:
            time.sleep(10)
        # If the notification doesn't go through after 10 attempts, raise an error.
        raise SlackNotificationError('Slack notification failed after 10 attempts.')
