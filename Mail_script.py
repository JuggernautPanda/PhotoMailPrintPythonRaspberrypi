#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Mail_script.py
#  
#  Copyright 2017 raja <raja@raja-Inspiron-N5110>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
import os
import smptlib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def MailMyPic():
    img_data = open('image.jpg', 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Foto_Lere! Picture of User'
    msg['From'] = 'hello@fotolere.com'
    msg['To'] = 'grajasumant@gmail.com'

    text = MIMEText("Yolo! Your picture is attached. Foto Lere! Fotolere, World's first free photo printing and delivery service, is about preserving photos because photos remind us of our memories, and our memories are priceless!")
    msg.attach(text)
    image2Mail = MIMEImage(img_data, name=os.path.basename('image.jpg'))
    msg.attach(image2Mail)

    s = smtplib.SMTP('smtp.zoho.com:587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    UserName = 'hello@fotolere.com'
    UserPassword = 'Theharsha@457'
    From = 'hello@fotolere.com'
    To = 'grajasumant@gmail.com'
    s.login(UserName, UserPassword)
    s.sendmail(From, To, msg.as_string())
    s.quit()

MailMyPic()

