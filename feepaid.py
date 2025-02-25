import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mails(complete_data):
    for data in complete_data:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        username = "xxxxxxxxxxxxx@gmail.com"
        password = "xxxx xxxx xxxx xxxx"

        from_email = "xxxxxxxxxxxxx@gmail.com"
        to_email = data[1]
        subject = "Fee Update"
        body = f"Dear {data[0]},\n\nOur records indicate that there is a pending fee associated with your account. \n\nWe kindly request you to clear the outstanding amount at your earliest convenience. If you have already made the payment, please disregard this message.\n\nFor any inquiries or assistance, feel free to reach out.\n\nBest regards,\n[Your Name/Organization]"


        msg = MIMEMultipart()
        msg['From'] = from_email    
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'plain'))

        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(username,password)
        server.send_message(msg)
        server.quit()
        print(f"Mail sent to {data[0]}")



