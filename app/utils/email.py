import os
import smtplib
from email.mime.text import MIMEText

from fastapi import HTTPException


async def send_verification_email(receiver_email: str, verification_code: str):
    try:
        # Set up the email message
        msg = MIMEText(f'Your verification code is {verification_code}')
        msg['Subject'] = 'Account Verification'
        msg['From'] = os.environ.get('SENDER_EMAIL')
        msg['To'] = receiver_email

        # Connect to the SMTP server
        async with smtplib.SMTP(os.environ.get('SMTP_SERVER'), int(os.environ.get('SMTP_PORT'))) as server:
            server.starttls()  # Enable TLS encryption
            server.login(os.environ.get('SMTP_USER'), os.environ.get('SMTP_PASSWORD'))
            server.sendmail(os.environ.get('SENDER_EMAIL'), receiver_email, msg.as_string())
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))