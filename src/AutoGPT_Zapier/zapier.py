"""This is a plugin to Zapier Webhooks for Auto-GPT"""
from pprint import pprint
import requests
import os


"""
Creates a new Webhook call to Zapier

Parameters:
    - title: The title of the page.
    - summary: A brief summary of the page.
    - content: The content of the page.

Returns:
    - If the page is created successfully, returns a string indicating the success
        and the URL of the newly created page.
    - If there is an error during the creation process, returns the error message.
"""

def call_webhook(title: str, summary: str, content: str):
    triggerUrl = os.getenv("ZAPIER_WEBHOOK_ENDPOINT")

    headers = {
        "content-type": "application/json",
    }

    payload = {
        "data": [
            {
                "title": title,
                "summary": summary,
                "content": content,
            },
        ]
    }

    response = requests.post(triggerUrl, headers=headers, json=payload, timeout=60)
    return response
