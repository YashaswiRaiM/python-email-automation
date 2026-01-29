import smtplib as s
ob= s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("raiyashaswi9@gmail.com","ysjb nxel rpeu hjxk")
subject="Test Python"
body="I love Python"
message="subject:{}\n\n{}".format(subject,body)
listadd=["junkmail@gmail.com",
         "saralamrai@gmail.com"]
ob.sendmail('raiyashaswi9@gmail.com',listadd,message)
print("send mail")
ob.quit()