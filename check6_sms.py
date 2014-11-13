# -*- coding: utf-8 -*-
import urllib2
import time
from twilio.rest import TwilioRestClient

mail_send = 0
ACCOUNT_SID = "ACc7cd037dfbd81fd6704c4db0dc7b6a5c"
AUTH_TOKEN = "43ae2b0ac6c817c6e2b36c000ebae524"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
while mail_send < 3:

    response = urllib2.urlopen('https://play.google.com/store/devices/details?id=nexus_6_blue_32gb')
    a = response.read()
    if 'We are out of inventory.' not in a or '<span class="play-button devices disabled">$649.00</span>' not in a :
        client.messages.create(body="Nexus 6!!!!!!!!!!!!!!!",
                    to="+8613128962965",
                    from_="+13306178660",
                    )
        mail_send += 1
        time.sleep(60)
