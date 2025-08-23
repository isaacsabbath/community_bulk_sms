# sms/services.py
import africastalking
import requests
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

# Correct import for the exception class

# OR, if that still doesn't work, try this:
# from africastalking.AfricasTalkingGateway import AfricasTalkingException 

# Load environment variables from .env file
load_dotenv()

def initialize_africastalking():
    """Initializes the Africa's Talking SDK with credentials from environment variables."""
    username = os.getenv("username")
    api_key = os.getenv("api_key")

    if not username or not api_key:
        print("Warning: Africa's Talking API credentials (AF_API_KEY or AF_USERNAME) are missing from your .env file.")
        return

    try:
        africastalking.initialize(username, api_key)
        print("Africa's Talking SDK initialized successfully.")
    except Exception as e:
        print(f"Error initializing Africa's Talking SDK: {e}")

def send_sms(message, recipients):
    """
    Sends an SMS message using the Africa's Talking SDK.
    Always returns a dict with status and message for consistency.
    """
    sms = africastalking.SMS
    try:
        response = sms.send(message, recipients)

        # Africa’s Talking returns a list of dicts (per recipient)
        # Example: [{'status': 'Success', 'messageId': '...', 'cost': 'KES 0.8000', 'number': '+2547...'}]

        if response and "SMSMessageData" in response:
            messages_data = response["SMSMessageData"]["Recipients"]

            # Check if at least one SMS succeeded
            if any(r.get("status") == "Success" for r in messages_data):
                return {"status": "success", "message": "Messages sent successfully"}
            else:
                return {"status": "error", "message": str(messages_data)}

        return {"status": "error", "message": "Invalid API response"}

    except Exception as e:
        # Log the error for debugging
        print(f"Error sending SMS: {e}")
        return {"status": "error", "message": str(e)}

# Initialize the SDK when the module is imported
initialize_africastalking()