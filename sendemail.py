import smtplib
  
emailid_list = ["nicksmeonly@gmail.com",]
for emailid in emailid_list:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("nicksmeonly@gmail.com", "narendrak")
    message = 'Subject: {}\n\n{}'.format('Welcome to Smartcomm', 'Hi, Welcome!')
    s.sendmail("sender_email_id", emailid, message)
    s.quit()