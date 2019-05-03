from execdash import to_usd, topsellers
import operator
import matplotlib.ticker as ty
import matplotlib.pyplot as mplp
import pandas as pd 
import os

def test_to_usd():
    result = to_usd(10)
    assert result == "$ 10.00"


def test_topsellers():
    
    numprodssec = 0
    yentry = "2019"
    month1 = "01"
    fname = "sales-" + yentry + month1 + ".csv"
    
    
    csvreader = pd.read_csv("data/" + fname)
    price = csvreader.groupby(csvreader['product']).sum()
    price = price.sort_values(by=['sales price'], ascending = False)
    productlist = []
    
    numprods = 0
    for n in csvreader['product']:
        if n not in productlist:
            numprods = numprods + 1
            
            productlist.append(n)


    

    
    #shoutout to @hiepnguyen034, learned how to do this from him

    
    result = topsellers(numprodssec, price)


    assert result == "1 - Button-Down Shirt       $ 5,659.35"
