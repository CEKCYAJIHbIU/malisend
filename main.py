import smtplib
from email.mime.text import MIMEText
from randomize import randomize

print('start')

raddr = 'maksobest@gmail.com'
print(raddr)
with open('emails.txt') as file:
    for mai in file:
        mail = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        print(mail.sock)
        laddr, _, lpass, _ = mai.split(':')
        mail.ehlo()

        msg = MIMEText(randomize("ОЧень важное сообщение, вас заминировали, вам пизда"), _charset='utf-8')
        msg.set_charset("utf-8")
        msg['From'] = f'"mina@mina.boom" <{laddr}>'
        msg['To'] = raddr
        msg['Subject'] = randomize("ВАЖНО!!!!!!!!")


        mail.login(laddr, lpass)
        print(mail.sendmail(laddr, [raddr], msg.as_string()), '-', laddr)
        mail.close()
