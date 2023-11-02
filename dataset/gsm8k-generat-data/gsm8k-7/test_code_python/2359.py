def solution():
    num_oranges = 25
    total_cost = 1250 # in cents

    selling_price = 60 # in cents
    revenue = num_oranges * selling_price

    profit = revenue - total_cost
    profit_per_orange = profit / num_oranges
    result = profit_per_orange
    return result

print(solution())