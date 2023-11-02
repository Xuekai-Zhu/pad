def solution():
    
    # Define the prices of Jairus and Jenny
    jairus_price = 0.8
    jenny_price = 0.5

    # Define the number of tasks
    num_tasks = 20

    # Calculate the total earnings for Jairus and Jenny
    jairus_earnings = jairus_price * num_tasks
    jenny_earnings = jenny_price * num_tasks

    # Calculate the difference in earnings between Jairus and Jenny
    earnings_difference = jairus_earnings - jenny_earnings

    # Return the result
    result = earnings_difference
    return result

print(solution())