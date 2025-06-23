import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def send_email(to_email, subject, message, fake_name, from_email="noreply@yourdomain.com"):
    api_key = os.getenv("SENDGRID_API_KEY")
    if not api_key:
        print("❌ SENDGRID_API_KEY not found in environment variables.")
        return

    mail = Mail(
        from_email=(from_email, fake_name),
        to_emails=to_email,
        subject=subject,
        plain_text_content=message
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(mail)
        print(f"✅ Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")

def run_cli():
    print("=== Anonymous Email CLI via SendGrid ===")
    to_email = input("Recipient Email: ").strip()
    fake_name = input("Fake Sender Name: ").strip()
    subject = input("Subject: ").strip()

    print("Write your message (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    message = "\n".join(lines)

    send_email(to_email, subject, message, fake_name)

if __name__ == "__main__":
    run_cli()




