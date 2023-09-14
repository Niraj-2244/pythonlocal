import smtplib as s

ob =s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('sahniraj276@gmail.com','prernaniraj2244')
subject="test python"
body= "i love python"
message="subject:{}\n\n".format(subject,body)
listad=['sahniraj276@gmail.com',
        "sahr56959@gmail.com"]
ob.sendmail('sahniraj276@gmail.com',listad,message)
print("send mail")
ob.quit()