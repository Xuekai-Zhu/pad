def solution():
    pies_baked = 200  # Du Chin bakes 200 meat pies in a day
    price_per_pie = 20  # He sells each pie for $20
    total_sales = pies_baked * price_per_pie  # Calculate the total sales for the day

    # Calculate the amount of money used to buy ingredients
    ingredient_cost = (3/5) * total_sales

    # Calculate the profit Du Chin remains with after buying ingredients
    remaining_profit = total_sales - ingredient_cost
    result = remaining_profit
    return result

print(solution())