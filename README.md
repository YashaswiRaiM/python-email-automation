# Python Email Automation Tool (Demo + Optional Safe Sending)

This repository contains **two Python projects** demonstrating automated email sending — from a **beginner approach** to a **professional automated workflow**.

---


## 1️. Beginner Version – Simple SMTP Email Sender

A basic script that sends plain text emails to multiple recipients using Python's `smtplib`.

### Code Example

```python
import smtplib as s

ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()
ob.login("raiyashaswi9@gmail.com","<AppPasswordHere>")
subject = "Test Python"
body = "I love Python"
message = "subject:{}\n\n{}".format(subject, body)

listadd = ["junkmail@gmail.com", "saralamrai@gmail.com"]

ob.sendmail('raiyashaswi9@gmail.com', listadd, message)
print("send mail")
ob.quit()

```

## Features

- Sends plain text emails
- Multiple recipients supported
- Demonstrates basic SMTP login and sending
- ⚠️ Use a Gmail App Password if 2-step verification is enabled.


---


## 2. Advanced Version – CSV-driven HTML Email Automation

This project demonstrates a **Python email automation tool** that prepares and optionally sends personalized emails with attachments and HTML content. Designed as a safe demo for automation and professional email handling.

## Features

- ✅ **CSV-driven automation** – Reads recipients from a CSV file for bulk email handling  
- ✅ **HTML email content** – Professional formatting, clickable links  
- ✅ **Attachments** – Supports sending files (e.g., `resume.pdf`)  
- ✅ **Demo mode** – Prints emails without sending; safe for testing  
- ✅ **Optional safe sending** – Use Gmail aliases (`yourname+test1@gmail.com`) to see emails in inbox  
- ✅ **Environment variable for App Password** – Secure and professional approach  

---

## 3. CSV Format Example

```csv
name,email
Test1,raiyashaswi9+test1@gmail.com
Test2,raiyashaswi9+test2@gmail.com
```

---

## 4. Usage

1. Place resume.pdf in the project folder.
2. Set your Gmail App Password as an environment variable:

Windows

```python
setx EMAIL_PASS "your_16_character_app_password"
```

Linux / MacOS:

```python
export EMAIL_PASS="your_16_character_app_password"
```

3. Run in demo mode (safe, prints emails instead of sending):

```python
python send_email.py
```

4. Optional: Send emails using Gmail aliases:

```python
send_email_safe(row["name"], row["email"], send_real=True)
```

- Use Gmail aliases like yourname+test1@gmail.com to prevent accidental sending.

---


## 5. Demo Output (Demo Mode)

```
✅ Email ready to send to Test1 (raiyashaswi9+test1@gmail.com)
   Subject: Hello from Python
   Attachment: resume.pdf
--------------------------------------------------
✅ Email ready to send to Test2 (raiyashaswi9+test2@gmail.com)
   Subject: Hello from Python
   Attachment: resume.pdf
--------------------------------------------------
```
