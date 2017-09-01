# Slackelot
Simple wrapper around the Slack Web API to post messages.

### Details
Slackelot contains a single function:
`send_message(message, webhook_url, pretext='', title='', author_name='', color=None)`

`webhook_url` should be in the following format:
`'https://hooks.slack.com/services/TEAM_ID/BOT_OR_CHANNEL_ID/AUTH_TOKEN'`

_Example_
```
from slackelot.slackelot import send_message


webhook_url = 'https://hooks.slack.com/services/TXXXXXXXX/BXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX'
message = 'Who wants to push the pram?\n@lancelot @percival'
pretext = 'Knights of the Round Table'
title = 'Spamelot'
author_name = 'Arthur'
color = '#663399'

send_message(message, webhook_url, pretext=pretext, title=title, author_name=author_name, color=color)
```

A nice feature for paid Slack teams is the option to mention another subteam, (ie. channel). In that
case, use the following syntax in your message:

`'\n<!subteam^ID|HANDLE>'`
(replace `ID` and `HANDLE` with your subteam's id and name, respectively).

For more information on message formatting, see the [Slack API docs](https://api.slack.com/docs/message-formatting)

### FAQ

[Where do I find my Slack team id?](https://api.slack.com/methods/team.info/test)

[Where do I find my Slack channel ids?](https://api.slack.com/methods/channels.list/test)

[Where do I create a  Slack auth token?](https://api.slack.com/tokens)

[How do I create a Slack bot user?](https://api.slack.com/bot-users)



