#!/usr/bin/env python3
import requests

def send_slack_message(webhook_url, message):
    """
    Send a message to Slack using an Incoming Webhook URL.
    
    Args:
        webhook_url (str): Slack Incoming Webhook URL.
        message (str): Message to send.
        
    Raises:
        ValueError: If the Slack API returns an error.
    """
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        raise ValueError(
            f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}"
        )
    print("Message sent successfully.")

if __name__ == "__main__":
    # Replace with your actual Slack Incoming Webhook URL.
    webhook_url = "https://hooks.slack.com/services/your/webhook/url"
    message = "Hello, this is a test message from Python."
    try:
        send_slack_message(webhook_url, message)
    except Exception as e:
        print(f"Failed to send message: {e}")
