# AlgorithmTrading

## Analysis of Stock Market Data with Python

 Through the analysis of the raw data, 
 we're gonna find out the meaningful indicators for the stocks

### 1. parsing_corp.py

 This code is for refining raw txt data into python data structure like list and dictionary.  
 I made records into lists and grouped them into dictionary based on company name.  
 So company names are the keys of dictionary and daily stock price records are values inside it.  
 Then First, I found out the market capitalization(stockPrice * num of shares) and computed log(mktCap).  
 Second, I searched for log(mktCap) each 1,2,3 years later from the base year.  
 Third, computed the growth rate of each record ( = log(mktCap) a year after / base year log(mktCap) - 1 ) * 100
