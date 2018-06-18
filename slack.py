'''
This is an example of how to send data to Slack webhooks in Python with the
requests module.
Detailed documentation of Slack Incoming Webhooks:
https://api.slack.com/incoming-webhooks

'''

import json
import requests
from firstlove.helpers import emailhandler
import time
import os

# Set the webhook_url to the one provided by Slack when you create the
# webhook at https://my.slack.com/services/new/incoming-webhook/


def post_to_channel(subject, text, color="#00ff00", time=time.time()):
    webhook_url = 'https://hooks.slack.com/services/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'
    icon = "https://academe.herokuapp.com/static/img/favicon.ico"
    homepage = "http://academe.herokuapp.com"
    slack_data = {
        "attachments": [
            {
                "fallback": text,
                "color": color,
                "author_link": homepage,
                "author_icon": icon,
                "title": subject,
                "title_link": homepage,
                "text": text,
                "footer": "Literature review",
                "footer_icon": icon,
                "ts": time
            }
        ]
    }

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        error_msg = 'Request to slack returned an error %s, the response is:\n%s' % (
            response.status_code, response.text)

        emailhandler.send_email("email", "Slack error", error_msg)