from Trading import API
from Trading.Ebest import login
from Trading.Ebest import config
from Trading.Ebest import api
from Trading.Ebest.transaction import query

import win32com, pythoncom


if __name__ == '__main__':

    Login = login.ebest_login()
    Login.connection_test()
    search_job = query.search("stock")
    search_job.stock_search("005930")
    search_job = query.search("candle")
    search_job.candle_search("005930","20211007","20211014")




