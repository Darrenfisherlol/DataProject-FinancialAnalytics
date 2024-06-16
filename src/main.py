'''
--
-- Author: Darren Fisher
-- Date: 6/15
--
-- What:
--  - This is the main file that will call and control how this code works
--
--
'''



'''
---------------------------------------------
--------------- Constants and Imports --------
---------------------------------------------
'''

import io
import json
import requests
import pandas as pd
import polars as pl
from urllib.request import urlopen


'''
---------------------------------------------
---------------------------------------------
---------------------------------------------
'''

def addData():
    print("add new data")


'''
---------------------------------------------
---------------------------------------------
---------------------------------------------
'''

def launchUI():
    print("launch GUI")

'''
---------------------------------------------
---------------------------------------------
---------------------------------------------
'''

def main():

    print("Hi\n 1.Input \'Add\' to add new data\n 2.Input \'Dash\' to showcase existing data")
    
    userInput = input()

    if userInput == "":
        launchUI()    
    elif userInput == "Add":
        addData()
    else:
        print("No Input, see you later alligator!")

'''
---------------------------------------------
--------------- Start Code ------------------
---------------------------------------------
'''

if __name__ == "__main__":
    main()

