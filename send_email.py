import smtplib
from email.message import EmailMessage

import getpass #password 보안 모듈
password = getpass.getpass('press your password HERE >> ')

email_list = ['phj5996@naver.com', 'phj5996@naver.com']

for address in email_list:
    msg = EmailMessage()
    msg['Subject'] = "오늘 점심은 뭐 나올까?" #제목
    msg['From'] = "tkdwns6114@naver.com" #발신자
    msg['To'] = address #송신자
    msg.set_content('''
                    식단표 좀 있었으면 좋겠다
                    그래야 오전에 좀 설레지
                    ''') #내용

smtp_url ='smtp.naver.com' #SMTP 서버명
smtp_port = 465 #SMTP 포트번호

s = smtplib.SMTP_SSL(smtp_url, smtp_port) #보안연결에 필요

s.login('tkdwns6114', password)
s.send_message(msg)