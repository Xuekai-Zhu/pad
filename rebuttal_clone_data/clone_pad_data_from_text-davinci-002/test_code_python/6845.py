def solution():
    cost_of_apples = 3
    cost_of_oranges = 2.70
    sale_price_of_apples = 10
    sale_price_of_oranges = 1
    total_cost = cost_of_apples + cost_of_oranges
    total_sale_price = sale_price_of_apples + sale_price_of_oranges
    profit = total_sale_price - total_cost
    return profit

print(solution())