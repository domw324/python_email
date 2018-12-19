import smtplib
from email.message import EmailMessage
import csv
import getpass #password 보안 모듈
password = getpass.getpass('press your password HERE >> ')

f = open('pygj.csv', 'r', encoding='utf-8')
read_csv = csv.reader(f)

smtp_url ='smtp.naver.com' #SMTP 서버명
smtp_port = 465 #SMTP 포트번호
s = smtplib.SMTP_SSL(smtp_url, smtp_port) #보안연결에 필요

s.login('tkdwns6114', password) #로그인

for line in read_csv:
    msg = EmailMessage()
    msg['Subject'] = line[0] + "님 안녕하세요, 테스트 중이니 양해 바랍니다ㅠㅠ" #제목
    msg['From'] = "tkdwns6114@naver.com" #발신자
    msg['To'] = line[1] #수신자
    msg.set_content('''
                    식단표 좀 있었으면 좋겠다..
                    그래야 오전에 좀 설레지
                    ''') #내용
    s.send_message(msg) #전송

f.close()