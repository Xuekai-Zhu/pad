def solution():
    shares_bought = 20
    shares_sold = 10
    price_bought = 3
    price_sold = 4
    shares_left = shares_bought - shares_sold
    price_doubled = price_bought * 2
    total_profit = (shares_sold * price_sold) + (shares_left * price_doubled) - (shares_bought * price_bought)
    result = total_profit
    return result

print(solution())