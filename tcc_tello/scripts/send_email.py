#!/usr/bin/env python3
"""
Envia email a partir de uma conta gmail com anexo.
"""

import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
  # cria o servidor SMTP
  context = ssl.create_default_context()
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls(context=context)
  server.ehlo()

  # dados do remetente
  sender_email = 'alertas.tcc.marcusalbano@gmail.com'
  password = 'tvlryemcpovimmld'

  # dados do destinatário
  receivers = ['alertas.tcc.marcusalbano@gmail.com']

  # dados do e-mail
  message = MIMEMultipart()
  message['Subject'] = 'Teste - Alerta!'
  message['From'] = sender_email
  message['To'] = ','.join(receivers)

  html = 'Alerta!!!'

  message.attach(MIMEText(html, 'html'))

  # define os atributos do anexo
  file = 'teste.png'
  filename = f'/home/marcus/Pictures/{file}'
  attachment = MIMEBase('application', 'octet-stream')

  with open(filename, 'rb') as f:
    attachment.set_payload(f.read())

  encoders.encode_base64(attachment)

  attachment.add_header(
    'Content-Disposition',
    f'attachment; filename={filename}',
  )

  # anexa o arquivo no e-mail
  message.attach(attachment)

  # realiza login no servidor
  server.login(sender_email, password)

  # envia o email
  server.sendmail(sender_email, receivers, message.as_string())

except Exception as e:
  print(f'Erros: {e}')
finally:
  # fecha o servidor
  server.quit()
