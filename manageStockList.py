#!/usr/bin/python3
import json
import os

from config import *

NO_INPUT        = 0
DISP_STOCKS     = 1
ADD_STOCKS      = 2


def ask_user(option=0):
    print("Hey, Welcome to StockPi!")
    print("1. Display Stocks")
    print("2. Add Stocks")

    if option == NO_INPUT:
        option = input("Plz tell what you want - ")
        try:
            option = int(option)
        except:
            print("Enter Valid Values")
            exit(1)

    if option == ADD_STOCKS:
        if os.path.exists(STOCK_FILE):
            data = json.load(STOCK_FILE)
        else:
            data = {}
        
        while True:
            name = input("Enter Stock Name - ")
            if name == '0':
                break
            units = input("Number of Units - ")
            units = int(units)
            # TODO:: Make this pretty


            if name in data.keys():
                data[name] = data[name] + units
            else:
                data[name] = units

        with open(STOCK_FILE, 'w+') as outfile:
            json.dump(data, outfile, sort_keys=True)
    
    else:
        print("Incorrect option")
        exit(0)
    
            
        



if __name__ == "__main__":
    ask_user()
