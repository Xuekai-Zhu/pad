def solution():
    # Calculate the cost to make 2 gallons of lemonade
    cost = 2 * 3.5

    # Calculate the number of glasses of lemonade that can be made
    glasses = 2 * 16

    # Calculate the total revenue from selling the glasses of lemonade
    revenue = (glasses - 5 - 6) * 1

    # Calculate the net profit
    net_profit = revenue - cost
    result = net_profit
    return result

print(solution())