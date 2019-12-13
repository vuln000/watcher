import smtplib

from email.mime.text import MIMEText


def send_alert_email(content):
	msg_from='237384893@qq.com'
	passwd='c*********tbigi'
	msg_to='237834893@qq.com'
	subject="alert email from your server"
	msg = MIMEText(content)
	msg['Subject'] = subject
	msg['From'] = msg_from
	msg['To'] = msg_to
	try:
		s = smtplib.SMTP_SSL("smtp.qq.com",465)
		s.login(msg_from, passwd)
		s.sendmail(msg_from, msg_to, msg.as_string())
		print "success"
	except:
		print 'error'
        s.quit()
#send_email('aaa')