def solution():
    num_sweaters = 28
    balls_per_sweater = 4
    cost_per_ball = 6
    selling_price = 35

    # Calculate the total number of balls of yarn needed for all sweaters
    total_balls_needed = num_sweaters * balls_per_sweater

    # Calculate the total cost of all balls of yarn needed
    total_yarn_cost = total_balls_needed * cost_per_ball

    # Calculate the total revenue from selling all the sweaters
    total_revenue = num_sweaters * selling_price

    # Calculate the total profit from selling all the sweaters
    total_profit = total_revenue - total_yarn_cost
    result = total_profit
    return result

print(solution())