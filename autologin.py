#!/usr/bin/env python

import os
import time
import mechanize

def recon():
    br = mechanize.Browser()

    br.set_handle_robots(False)
    br.open('http://192.168.1.1/platform.cgi?page=captivePortal.htm')

    response = br.response()
    headers = response.info()
    # that crappy repeater doesn't even reply the correct content-type
    headers["Content-type"] = "text/html; charset=utf-8"

    br.select_form(nr=0)

    br.form['CaptivePortalSession.UserName'] = 'myuser'
    br.form['CaptivePortalSession.Password'] = 'mypasswd'

    br.submit()

    print br.response().info()

while True:
    # yeah well, I'm not running for the best script of the year ok?
    r = os.system('ping -c 1 8.8.8.8')
    if r != 0:
        recon()
    time.sleep(5)
