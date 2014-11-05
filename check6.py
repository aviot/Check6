# -*- coding: utf-8 -*-
import urllib2
import time
import smtplib
mail_send = 0
while mail_send < 3:

    response = urllib2.urlopen('https://play.google.com/store/devices/details?id=nexus_6_blue_32gb')
    a = response.read()
    if 'We are out of inventory.' not in a or '<span class="play-button devices disabled">$649.00</span>' not in a :
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("checknexus666", "123456qwe123")
        msg = "Nexus 6 is on sale!!!!!\nHurry up!!! %s" % a # The /n separates the message from the headers
        server.sendmail("checknexus666@gmail.com", "aviotster@gmail.com", msg)
        server.close()
        mail_send += 1
        time.sleep(60)
