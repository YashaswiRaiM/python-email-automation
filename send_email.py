import csv
import os
import smtplib
from email.message import EmailMessage

# -----------------------------
# Configuration
EMAIL = "raiyashaswi9@gmail.com"
PASSWORD = os.getenv("EMAIL_PASS")  # App password stored as environment variable
SUBJECT = "Hello from Python"
ATTACHMENT_PATH = "Resume_Yashaswi Rai M.pdf"
HTML_CONTENT = """
<h2 style='color:blue;'>Hi {name}!</h2>
<p>This is an <b>automated email</b> sent using Python.</p>
<p>Check out my <a href='https://www.linkedin.com/in/yashaswi-rai-m-50069b357/'>LinkedIn</a>.</p>
"""

# -----------------------------
def send_email_safe(receiver_name, receiver_email, send_real=True):
    """Send real email if send_real=True, otherwise just print demo output."""
    msg = EmailMessage()
    msg["Subject"] = SUBJECT
    msg["From"] = EMAIL
    msg["To"] = receiver_email
    msg.add_alternative(HTML_CONTENT.format(name=receiver_name), subtype="html")

    # Attach resume if exists
    if os.path.exists(ATTACHMENT_PATH):
        with open(ATTACHMENT_PATH, "rb") as f:
            msg.add_attachment(f.read(),
                               maintype="application",
                               subtype="octet-stream",
                               filename=ATTACHMENT_PATH)

    if send_real:
        # Send using Gmail SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        print(f"✅ Real email sent to {receiver_name} ({receiver_email})")
    else:
        # Demo output
        print(f"✅ Email ready to send to {receiver_name} ({receiver_email})")
        print(f"   Subject: {SUBJECT}")
        if os.path.exists(ATTACHMENT_PATH):
            print(f"   Attachment: {ATTACHMENT_PATH}")
        print("-"*50)

# -----------------------------
# Read recipients from CSV
with open("receivers.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Change this flag to True to actually send emails
        send_email_safe(row["name"], row["email"], send_real=False)

