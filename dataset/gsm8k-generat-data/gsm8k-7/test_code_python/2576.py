def solution():
    num_gallons = 2
    glasses_per_gallon = 16
    cost_per_gallon = 3.5
    sell_price_per_glass = 1.0
    glasses_drunk = 5
    glasses_left = 6

    # Calculate the total number of glasses of lemonade that Brad made
    total_glasses = num_gallons * glasses_per_gallon

    # Calculate the cost of making all the lemonade
    total_cost = num_gallons * cost_per_gallon

    # Calculate the total revenue from selling the lemonade
    total_revenue = ((total_glasses - glasses_drunk) - glasses_left) * sell_price_per_glass

    # Calculate net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())