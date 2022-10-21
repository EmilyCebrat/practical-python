# report.py
#
# Exercise 2.4
from pprint import pprint
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio_dict = {}
            portfolio_dict['name'] = row[0]
            portfolio_dict['shares'] = int(row[1])
            portfolio_dict['price'] = float(row[2])
            portfolio.append(portfolio_dict)
    return portfolio

def read_prices(filename):

    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if len(row) > 0:
                name = row[0]
                price = float(row[1])
                if name not in prices.keys():
                    prices[name] = price
    return prices

def gainloss(portfolio_file, prices_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    
    my_total_cost = 0.0
    market_cost_now = 0.0
    for tuple in portfolio:
         my_total_cost += tuple['shares'] * tuple['price']
         if tuple['name'] in prices:
             name = tuple['name']
             market_cost_now += tuple['shares'] * prices[name] 

    gainloss = round((market_cost_now - my_total_cost), 2)

    print(f'I bought my shares for {my_total_cost} and the shares are now worth {market_cost_now} so I gained/lost {gainloss}') 

def makereport(portfolio_file, prices_file):
    
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    

    change = 0.0
    for tuple in portfolio:
         if tuple['name'] in prices:
             change = prices[tuple['name']]  - tuple['price']
         print(f'{tuple["name"]:10s} {tuple["shares"]:>10d} {tuple["price"]:>10.2f} {change:>10.2f}')
    


makereport('/Users/cebratm/Documents/Python-Practice/practical-python/Work/Data/portfolio.csv', '/Users/cebratm/Documents/Python-Practice/practical-python/Work/Data/prices.csv')





#gainloss('/Users/cebratm/Documents/Python-Practice/practical-python/Work/Data/portfolio.csv', '/Users/cebratm/Documents/Python-Practice/practical-python/Work/Data/prices.csv')    


#result = read_prices('/Users/cebratm/Documents/Python-Practice/practical-python/Work/Data/prices.csv')

#read_portfolio(filename)        
#read_portfolio('/Users/cebratm/Documents/Python-Practice/practical-python/Work/Data/portfolio.csv')



