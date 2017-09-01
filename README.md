# Slackelot
Simple wrapper around the Slack Web API to post messages.

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



