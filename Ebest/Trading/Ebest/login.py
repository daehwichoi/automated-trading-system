import os
from . import config
import win32com.client
import pythoncom


class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")

class ebest_login:

    def __init__(self):
        self.connection_try()

    def connection_try(self):
        self.ID = input("ID:")
        self.PW = input("PW:")
        self.cert_PW = input("Cert PW:")

    def connection_test(self):
        instXASession = win32com.client.DispatchWithEvents(config.SESSION_CLIENT_NAME, XASessionEventHandler)
        instXASession.ConnectServer(config.EBEST_SITE, 20001)
        instXASession.Login(self.ID, self.PW, self.cert_PW, 0, 0)
        self.connection_check()


    def connection_check(self):
        while XASessionEventHandler.login_state == 0:
            pythoncom.PumpWaitingMessages()
        return True







