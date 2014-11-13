# -*- coding: utf-8 -*-
import urllib2
import time
from twilio.rest import TwilioRestClient

mail_send = 0
ACCOUNT_SID = [ACCOUNT_SID]
AUTH_TOKEN = [AUTH_TOKEN]
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
while mail_send < 10:

    response = urllib2.urlopen('https://play.google.com/store/devices/details?id=nexus_6_blue_32gb')
    a = response.read()
    if 'We are out of inventory.' not in a and '<span class="play-button devices disabled">$649.00</span>' not in a :
        client.messages.create(body="Nexus 6!!!!!!!!!!!!!!!",
                    to="+country_code+phone",
                    from_="+twilio_number",
                    )
        mail_send += 1
        time.sleep(60)
