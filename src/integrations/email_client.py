import smtplib
from email.message import EmailMessage


class EmailClient:
    """
    电子邮件客户端，用于发送电子邮件。

    方法:
    - send_email: 发送电子邮件。
    """

    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, body):
        """
        发送电子邮件。

        :param recipient: 收件人地址。
        :param subject: 邮件主题。
        :param body: 邮件正文。
        """
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = recipient

        with smtplib.SMTP(self.server, self.port) as server:
            server.login(self.username, self.password)
            server.send_message(msg)
