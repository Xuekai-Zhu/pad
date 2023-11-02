def solution():
    
    num_newspapers = 500
    sale_price = 2
    percent_sold = 80
    num_sold = num_newspapers * (percent_sold / 100)
    purchase_price = sale_price * (1 - 0.75)
    cost = num_newspapers * purchase_price
    revenue = num_sold * sale_price
    profit = revenue - cost
    result = profit
    return result

print(solution())