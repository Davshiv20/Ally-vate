import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from ranks import rank


def send_email(subject, body, to_email, pdf_attachment_path=None):
    # Replace with your email and password
    sender_email = "shivamdave2903@gmail.com"
    password = "hnsh ilvd xgea wbcv"

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Attach the body to the message
    message.attach(MIMEText(body, "plain"))

    # Attach the PDF file
    if pdf_attachment_path:
        with open(pdf_attachment_path, "rb") as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="txt")
            pdf_attachment.add_header("Content-Disposition", f"attachment; filename={pdf_attachment_path}")
            message.attach(pdf_attachment)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to the SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, to_email, message.as_string())
            print("Email with attachment sent.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
# send_email("Subject", "Body", "recipient@example.com", "path_to_attachment.pdf")
