from execdash import to_usd, topsellers
import operator
import matplotlib.ticker as ty
import matplotlib.pyplot as mplp
import pandas as pd 
import os

def test_to_usd():
    result = to_usd(10)
    result1 = to_usd(1000)
    result2 = to_usd(57.3333)
    result3 = to_usd(.011111111)
    assert result == "$ 10.00"
    assert result1 == "$ 1000.00"
    assert result2 == "$ 57.33"
    assert result3 == "$ 0.01"

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
