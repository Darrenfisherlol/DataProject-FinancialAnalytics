'''
--
-- Author: Darren Fisher
-- Date: 6/15
--
-- What:
--  - This is the equity file which controls the main Equity class
--
--
'''


'''
---------------------------------------------
--------------- Class -----------------------
---------------------------------------------
'''


class Equity:

    def __init__(self, ticker):
        self.ticker = ticker

        # income statement
        self.IncomeStatement = []

        #  cash flow
        self.cashFlow = []

        #  price
        self.price = []
        
        # volume
        self.volumeInsider = []
        self.gov = []        

    def getTicker(self):
        return self.ticker
    
    # Income Statement getter and setter
    def getIncomeStatement(self):
        return self.IncomeStatement 

    def setIncomeStatement(self, df):
        self.IncomeStatement.append(df) 

    # Cash Flow getter and setter
    def getcashFlow(self):
        return self.cashFlow 

    def setcashFlow(self, df):
        self.cashFlow.append(df)  

    # Price getter and setter
    def getPrice(self):
        return self.price 

    def setPrice(self, df):
        self.price.append(df) 

