#!/usr/bin/python

from ServerStatus import *

SSL_VERIFYHOST = 0;
SSL_VERIFYPEER = 0
SSL_CA = ""

SMTP_SERVER = "localhost"

FROM_ADDRESS = "example@example.com"
TO_ADDRESSES = ["example@example.com"]


Servers = [Server("https://www.google.com", TO_ADDRESSES)]

server_tester = ServerTester( CurlTester(SSL_VERIFYHOST, SSL_VERIFYPEER, SSL_CA ), [SimpleEmailNotifier(from_address=FROM_ADDRESS, smtp_server=SMTP_SERVER), PrintNotifier()], True )

server_tester.test(Servers)