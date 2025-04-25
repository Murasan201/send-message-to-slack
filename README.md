# Send a Message to Slack

This repository contains a simple Python test program to send messages to a Slack channel using an Incoming Webhook.

## Overview

The program is implemented in the `slack-msg-test.py` script. It uses the [requests](https://pypi.org/project/requests/) library to post a message to Slack via an Incoming Webhook URL.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Murasan201/send-message-to-slack.git
   cd send-message-to-slack
   ```

2. **Install Dependencies**

   Ensure you have Python 3 installed. Install the required dependencies:
   
   ```bash
   python -m pip install requests
   ```

3. **Configure Slack Webhook**
   
   In the file `slack-msg-test.py`, update the `webhook_url` variable with your actual Slack Incoming Webhook URL:
   
   ```python
   webhook_url = "https://hooks.slack.com/services/your/webhook/url"
   ```

## Usage

Run the script to send a test message to Slack:

```bash
python slack-msg-test.py
```

If the message is sent successfully, you will see the output:

```
Message sent successfully.
```

If there is an error, it will print an error message.

## License

This project is licensed under the MIT License.
