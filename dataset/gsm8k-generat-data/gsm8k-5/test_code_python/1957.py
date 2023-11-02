def solution():
    newspapers_bought = 500
    price_per_newspaper = 2
    sales_percentage = 0.8
    cost_percentage = 0.75

    # Calculate the total amount spent to buy the newspapers
    total_cost = newspapers_bought * price_per_newspaper * (1 - cost_percentage)

    # Calculate the total revenue from selling 80% of the newspapers
    total_revenue = newspapers_bought * price_per_newspaper * sales_percentage

    # Calculate the profit
    profit = total_revenue - total_cost

    result = profit
    return result

print(solution())