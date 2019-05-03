import operator
import matplotlib.ticker as ty
import matplotlib.pyplot as mplp
import pandas as pd 
import os

def to_usd(i):
    delta = "$ {0:.2f}".format(i)
    return delta


def topsellers(numprodssec, price):
    

    countvar = str(numprodssec + 1) 
    totsales = str("{0:,.2f}".format(price.iloc[numprodssec][2])).rjust(9)
    prodname = str(price.index[numprodssec]).ljust(20)
    hsellinglist = countvar + " - " + prodname + "    $" + totsales
    print(hsellinglist)
    
    return hsellinglist

def mreturn(monthalpha):
    #this function allows a month to be selected from the dictionary after the user enters a number for the month later in the program
        calendar = {'01':'January','02':'February','03':'March','04':'April', '05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
        return calendar[monthalpha]    

    
#allowing pytest to occur via line below to separate functions from main
        
if __name__ == "__main__":


    print("Thank you for using the Executive Dashboard Helper Tool")
    print("----------------------------------------")
    print("Please follow the instructions closely in order to enjoy an optimal experience")
    print("Furthermore, ensure that your monthly sales files are organized in the 'Data' folder")
    print("----------------------------------------")

    while True:
    #this chunk of code allows the user to enter a month and year instead of having to know the exact filenames and naming conventions

        monthalpha = input("Using the format MM (for example: January is 01), please enter the month for your sales data of choice:      ")
        yentry = input("Using the format YYYY, please enter the year for your sales data of choice:      ")

        fname = "sales-" + yentry + monthalpha + ".csv"

        if not os.path.isfile("data/" + fname):
            print("Error: data does not exist for the month and year you entered. The file could not be found. Please restart.")
            #error message that appears if the file does not exist
        else:
            break

    month = mreturn(monthalpha)


    #This part of the code reads the csv and then distinguishes between the products, creating a list for each one
    #Follows up by creating a sales prices for each, creates total prices at the end by summing them up
    csvreader = pd.read_csv("data/" + fname)
    productlist = []

    #the following variables are variables used for counting later on
    numprods = 0
    numprodssec = 0

    for n in csvreader['product']:
        if n not in productlist:
            numprods = numprods + 1
            productlist.append(n)

    price = csvreader.groupby(csvreader['product']).sum()

    price = price.sort_values(by=['sales price'], ascending = False)
    #shoutout to @hiepnguyen034, learned how to do this from him

    totalprice = price['sales price'].sum()
    #totalprice = price.sort_values(by=[totalprice], ascending = False)

    #GRAPH RELATED MATERIALS

    graphlist = []
    #allows for entries of prices


    salep = 0
    while salep < numprods:
        graphlist.append(price.iloc[salep][2])
        salep = salep + 1




    print(" ")

    print("----------------------------------------")
    print(" ")

    print("MONTH: " + month + " " + yentry)
    print(" ")

    print("----------------------------------------")
    print(" ")

    print("CALCULATING...")
    print(" ")

    print("----------------------------------------")
    print(" ")

    print("TOTAL MONTHLY SALES: $" + str("{0:,.2f}".format(totalprice)))
    print(" ")

    print("----------------------------------------")
    print("TOP SELLING PRODUCTS")


    #outputs highest selling products, their ranking, and how much sales were
    while numprodssec < numprods:
        #countvar = str(numprodssec + 1) 
        #totsales = str("{0:,.2f}".format(price.iloc[numprodssec][2])).rjust(9)
        #prodname = str(price.index[numprodssec]).ljust(20)
    
        #hsellinglist = countvar + " - " + prodname + "    $" + totsales
        #print(hsellinglist)
        #allows program to continue in a loop ]
        #numprodssec = numprodssec + 1
        topsellers(numprodssec, price)
        numprodssec = numprodssec + 1

    print("----------------------------------------")

    print(" ")

    #graph creation pulls data from list earlier named "graphlist" to create the visualized data
    print("VISUALIZING THE DATA...")

    fig, bgraph = mplp.subplots()
    fig.set_figheight(5)
    fig.set_figwidth(15)
    #formatting of graph dimensions

    for uno, dos in enumerate(graphlist):
        bgraph.text(dos, uno, " ${0:,.2f}".format(dos)).set_fontsize(7)
    #shoutout to an assortment of stack overflow pages, a conversation with a CS TA, and a phone call with my friend who majors in CS

    datapull = price.index.tolist()
    dashes = ty.StrMethodFormatter("{x:,.2f}")
    bgraph.xaxis.set_major_formatter(dashes)
    #Shoutout @chenmi1997 for help with the formatting here


    bgraph.barh(datapull,graphlist)
    #pulls the data into the bar graph


    #setting labels for the chart
    bgraph.set_xlabel("Sales ($)")
    bgraph.set_ylabel("Product")

    bgraph.set_title(month + " " + yentry + " - Highest Selling Products ") 

    mplp.tight_layout()
    #shoutout to https://georgetown-opim-py.slack.com/archives/CFZDKNKA4/p1549983772015200


    print(" ")
    print("----------------------------------------")
    print(" ")
    print("Thank you for using the Executive Dashboard!")

    mplp.show()

