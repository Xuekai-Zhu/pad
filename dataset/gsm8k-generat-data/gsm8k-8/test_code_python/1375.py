def solution():
    # Calculate the total cost of feeding each piglet for 12 months
    piglet_food_cost_12_months = 12 * 10

    # Calculate the total cost of feeding each piglet for 16 months
    piglet_food_cost_16_months = 16 * 10

    # Calculate the total cost of feeding all 6 piglets before they are sold
    total_food_cost = 6 * (piglet_food_cost_12_months + piglet_food_cost_16_months)

    # Calculate the total revenue from selling all 6 fully grown pigs
    total_revenue = 6 * 300

    # Calculate the total profit after deducting the cost of food
    total_profit = total_revenue - total_food_cost
    result = total_profit
    return result

print(solution())