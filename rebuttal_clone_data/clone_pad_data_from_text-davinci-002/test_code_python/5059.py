def solution():
    percent_sold = 80
    toys_bought = 200
    toys_sold = percent_sold * toys_bought / 100
    initial_cost = toys_bought * 20
    sale_price = toys_sold * 30
    profit = sale_price - initial_cost
    result = profit
    return result

print(solution())