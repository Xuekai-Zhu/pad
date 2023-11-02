def solution():
    # Calculate the total cost of making 2 gallons of lemonade
    cost = 3.50 * 2  # it costs $3.50 to make one gallon of lemonade

    # Calculate the total number of glasses of lemonade Brad made
    num_glasses = 2 * 16  # one gallon yields 16 glasses

    # Calculate the total amount of money Brad earned from selling lemonade
    total_earnings = (num_glasses - 5 - 6) * 1.00  # Brad drank 5 glasses and had 6 remaining

    # Calculate the net profit Brad earned
    net_profit = total_earnings - cost

    result = net_profit
    return result

print(solution())