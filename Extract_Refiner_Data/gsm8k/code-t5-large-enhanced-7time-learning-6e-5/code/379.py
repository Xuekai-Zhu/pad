def solution():
    
    # Define the cost of supplies and the number of pitchers
    supplies_cost = 18
    num_pitchers = 3

    # Calculate the total number of cups of lemonade needed
    total_cups = num_pitchers * 12

    # Calculate the total revenue from selling all the lemonade
    total_revenue = total_cups * 1

    # Calculate the total time spent running the lemonade stand
    total_time = total_cups / 4

    # Calculate the profit per hour
    profit_per_hour = total_revenue - supplies_cost

    # Display the profit per hour
    result = profit_per_hour
    return result

print(solution())