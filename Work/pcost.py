# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):


    total_cost = 0.0
    

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:

            price = row[2]
            share_amount = row[1]
            try:
                if price=='' or share_amount=='':
                    raise ValueError('empty string')
                else:
                    total_cost = total_cost + (float(price)*int(share_amount))
            except ValueError as e:
                print(e)     

    print(f'Total cost: ${total_cost}')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "/Users/cebratm/Documents/Python-Practice/practical-python/Work/Data/portfolio.csv"


portfolio_cost(filename)

