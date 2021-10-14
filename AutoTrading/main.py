import win32com.client
import os

class Auto_stock_controller:
    def __init__(self):
        print("Connceting...")
        connect_CpCybos = win32com.client.Dispatch("CpUtil.CpCybos")

        # Connect Check
        isConnect = connect_CpCybos.IsConnect
        if isConnect == 9:
            print("Fail Connect")
        else:
            print("Success Connect")

            # 종목 정보 형태 call

            instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
            instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

            # Stock Num List DB화 (Excel)

            instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
            codelist = instCpCodeMgr.GetStockListByMarket(1)
            kospi = {}

            for code in codelist:
                name = instCpCodeMgr.CodeToName(code)
                kospi[code] = name

            f = open(os.getcwd() + "\kospi.csv", "w")
            for key, value in kospi.items():
                f.write("%s,%s\n" % (key, value))
            f.close()

            # 정보 Extract

            stockNum = instCpStockCode.GetCount()

            for i in range(stockNum):
                if instCpStockCode.GetData(0, i) in "A005930":
                    print(instCpStockCode.GetData(1, i), instCpStockCode.GetData(0, i))
                    instStockChart.SetInputValue(0, instCpStockCode.GetData(0, i))
                    instStockChart.SetInputValue(1, ord("2"))
                    instStockChart.SetInputValue(4, 10)
                    instStockChart.SetInputValue(5, (0, 4, 5))
                    instStockChart.SetInputValue(6, ord("D"))
                    instStockChart.SetInputValue(9, ord("1"))
                    instStockChart.BlockRequest()

                    numData = instStockChart.GetHeaderValue(3)
                    numField = instStockChart.GetHeaderValue(1)

                    for j in range(numData):
                        for k in range(numField):
                            print(instStockChart.GetDataValue(k, j), end=" ")
                        print("")


Auto_stock_controller()
