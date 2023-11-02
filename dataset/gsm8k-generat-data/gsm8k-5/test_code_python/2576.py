def solution():
    cost_per_gallon = 3.50  # It costs Brad $3.50 to make a gallon of lemonade
    glasses_per_gallon = 16  # Each gallon of lemonade yields 16 glasses

    # Calculate the cost of making 2 gallons of lemonade
    total_cost = cost_per_gallon * 2

    # Calculate the revenue from selling the lemonade
    total_revenue = (glasses_per_gallon * 2 - 5 - 6) * 1.00

    # Calculate the net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())