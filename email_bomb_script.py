import smtplib

email_address = "" #any gmail       
email_password = "" #use apppassowrd
target ="" #target email
counter = 0
while counter < 100 :
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        smtp.login(email_address, email_passowrd)
        subject = "Enter Any Subject"
        body = "Enter Any body"
        
        msg = f"Subject: {subject}\n\n{body}"
        
        smtp.sendmail(email_address, target , msg)
    counter += 1
