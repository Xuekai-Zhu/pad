def solution():
    bought_price = 50
    sold_price = 30
    dozens_sold = 50
    profit = (sold_price / 2) * dozens_sold - bought_price * dozens_sold
    result = profit
    return result

print(solution())