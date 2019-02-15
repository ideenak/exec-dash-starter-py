import operator
import matplotlib.pyplot as mplp
import pandas as pd 
import os

print("Thank you for using the Executive Dashboard Helper Tool")
print("----------------------------------------")
print("Please follow the instructions closely in order to enjoy an optimal experience")
print("Furthermore, ensure that your monthly sales files are organized in the 'Data' folder")
print("----------------------------------------")

def mreturn(monthalpha):
#this function allows a month to be selected from the dictionary after the user enters a number for the month later in the program
    calendar = {'01':'January','02':'February','03':'March','04':'April', '05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
    return calendar[monthalpha]


while True:
#this chunk of code allows the user to enter a month and year instead of having to know the exact filenames and naming conventions

    monthalpha = input("Using the format MM (for example: January is 01), please enter the month for your sales data of choice:      ")
    yentry = input("Using the format YYYY, please enter the year for your sales data of choice:      ")

    fname = "sales-" + yentry + monthalpha + ".csv"
