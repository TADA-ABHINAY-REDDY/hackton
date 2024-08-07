import smtplib
from email.mime.text import MIMEText
import requests

def send_email_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Suspicious Activity Detected'
    msg['From'] = 'b21cn004@kitsw.ac.in'  # Replace with your email
    msg['To'] = 'tada18reddy@example.com'  # Replace with recipient email

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'b21cn004@kitsw.ac.in'  # Replace with your email
    smtp_password = '12ab89hi'  # Replace with your app-specific password

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
        print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Failed to authenticate with the SMTP server: {e}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_sms_alert(message):
    api_key = 'NzU1OTZmNGU0NzRmNTAzNzUzNzA0NjZhNDgzNjMxNjY='
    sender = 'MYBIZ1'  # Replace with TextLocal approved sender ID
    numbers = '917893107738'  # Replace with the recipient's number in India
    url = 'https://api.textlocal.in/send/'

    params = {
        'apikey': api_key,
        'numbers': numbers,
        'message': message,
        'sender': sender
    }

    response = requests.post(url, params=params)
    response_data = response.json()

    if response_data['status'] == 'success':
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['errors'][0]['message']}")

if __name__ == "__main__":
    message = "Hello, this is a test message"
    send_email_alert(message)
    send_sms_alert(message)
