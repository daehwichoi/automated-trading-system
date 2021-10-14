import win32com.client
import pythoncom

from .. import config
from .query_list.query_handler import *



class search:
    def __init__(self, content):

        if content == "stock":
            res_file = "t1102"
        elif content == "candle":
            res_file = "t8413"

        self.file_path = f"{config.API_PATH}{res_file}.res"

        print(f"{content} Query Connection...")


    def stock_search(self,code):

        instXAQueryT1102 = win32com.client.DispatchWithEvents(config.QUERY_CLIENT_NAME, XAQueryEventHandlerT1102)
        instXAQueryT1102.ResFileName = self.file_path
        instXAQueryT1102.SetFieldData("t1102InBlock", "shcode", 0, code)
        instXAQueryT1102.Request(0)

        while XAQueryEventHandlerT1102.query_state == 0:
            pythoncom.PumpWaitingMessages()

        name = instXAQueryT1102.GetFieldData("t1102OutBlock", "hname", 0)
        price = instXAQueryT1102.GetFieldData("t1102OutBlock", "price", 0)
        print(name)
        print(price)

        return name, price

    def candle_search(self,code,start,end):

        instXAQueryT8413 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT8413)
        instXAQueryT8413.ResFileName = self.file_path

        instXAQueryT8413.SetFieldData("t8413InBlock", "shcode", 0, code)
        instXAQueryT8413.SetFieldData("t8413InBlock", "gubun", 0, "2")
        instXAQueryT8413.SetFieldData("t8413InBlock", "sdate", 0, start)
        instXAQueryT8413.SetFieldData("t8413InBlock", "edate", 0, end)
        instXAQueryT8413.SetFieldData("t8413InBlock", "comp_yn", 0, "N")

        instXAQueryT8413.Request(0)

        while XAQueryEventHandlerT8413.query_state == 0:
            pythoncom.PumpWaitingMessages()

        count = instXAQueryT8413.GetBlockCount("t8413OutBlock1")
        for i in range(count):
            date = instXAQueryT8413.GetFieldData("t8413OutBlock1", "date", i)
            open = instXAQueryT8413.GetFieldData("t8413OutBlock1", "open", i)
            high = instXAQueryT8413.GetFieldData("t8413OutBlock1", "high", i)
            low = instXAQueryT8413.GetFieldData("t8413OutBlock1", "low", i)
            close = instXAQueryT8413.GetFieldData("t8413OutBlock1", "close", i)
            print(date, open, high, low, close)

        return date, open, high, low, close
