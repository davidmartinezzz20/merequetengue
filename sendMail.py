import smtplib
from email.mime.text import MIMEText
from settings import importantKey
from mailBody import mailBody

# Define the subject and body of the email.
subject = "This is your periodical news wrap up."
body = mailBody
# Define the sender's email address.
sender = "elmeseherodedios@gmail.com"
# List of recipients to whom the email will be sent.
recipients = ["opt1a.david.martinez@gmail.com"]
# Password for the sender's email account.
password = importantKey

def send_email(subject, body, sender, recipients, password):
    # Create a MIMEText object with the body of the email.
    msg = MIMEText(body, 'html')
    # Set the subject of the email.
    msg['Subject'] = subject
    # Set the sender's email.
    msg['From'] = sender
    # Join the list of recipients into a single string separated by commas.
    msg['To'] = ', '.join(recipients)
   
    # Connect to Gmail's SMTP server using SSL.
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        # Login to the SMTP server using the sender's credentials.
        smtp_server.login(sender, password)
        # Send the email. The sendmail function requires the sender's email, the list of recipients, and the email message as a string.
        smtp_server.sendmail(sender, recipients, msg.as_string())
    # Print a message to console after successfully sending the email.
    print("Message sent!")

# Call the function to send the email.
send_email(subject, body, sender, recipients, password)