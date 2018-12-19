import smtplib
from email.message import EmailMessage

import getpass #password 보안 모듈
password = getpass.getpass('press your password HERE >> ')

msg = EmailMessage()
msg['Subject'] = "오늘 점심은 뭐 나올까?" #제목
msg['From'] = "tkdwns6114@naver.com" #발신자
msg['To'] = "phj5996@naver.com" #수신자
#msg.set_content('ㅈㄱㄴ') #내용
msg.add_alternative('''
<h1>안녕하세요!!</h1>
<p>저는 서상준 입니다.</p>
''', subtype="html")

smtp_url ='smtp.naver.com' #SMTP 서버명
smtp_port = 465 #SMTP 포트번호

s = smtplib.SMTP_SSL(smtp_url, smtp_port) #보안연결에 필요

s.login('tkdwns6114', password)
s.send_message(msg)