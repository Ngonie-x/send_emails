import re
import smtplib

EMAIL_REGEX = re.compile(r'.*@.*\.com')


#using regular expressions to make sure correct email addresses are entered into the recipients section
def check_recipients(recipients_string):
    #split the email addresses by a comma
    # receivers = recipients_string.split(",")
    emails = EMAIL_REGEX.findall(recipients_string)
    for email in emails:
        print(email)
    return emails

def send_email(email, password, recipients, subject, text):
    try:
        print("Connecting to smtp server...")
        smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
        print("Starting connection...")
        smtp_obj.ehlo()

        smtp_obj.starttls()
        
        print("Trying to log in...")
        smtp_obj.login(email, password)
        print("Logged in...")

        print("Trying to send the email...")
        smtp_obj.sendmail(email, recipients, f'Subject: {subject}\n{text}')
        print("Email has been sent!")

        smtp_obj.quit()
        print("Connection has been closed!")
    
    
    except Exception as e:
        print(e)