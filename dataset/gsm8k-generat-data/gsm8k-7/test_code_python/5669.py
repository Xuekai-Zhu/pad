def solution():
    buying_price = 600
    daily_food_cost = 20
    vaccination_cost = 500
    selling_price = 2500
    num_days = 40

    # Calculate the total cost of keeping the cow for 40 days
    total_cost = buying_price + (daily_food_cost * num_days) + vaccination_cost

    # Calculate the profit made from selling the cow
    profit = selling_price - total_cost
    result = profit
    return result

print(solution())