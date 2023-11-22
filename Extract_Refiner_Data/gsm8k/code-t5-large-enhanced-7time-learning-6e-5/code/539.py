def solution():
    
    # Define the prices for each task
    JAIRUS_PRICE = 0.8
    JENNY_PRICE = 0.5

    # Define the number of tasks each person finished
    num_tasks = 20

    # Calculate the total earnings for each person
    jairus_earnings = num_tasks * JAIRUS_PRICE
    jenny_earnings = num_tasks * JENNY_PRICE

    # Calculate the difference in earnings between Jairus and Jenny
    difference = jairus_earnings - jenny_earnings

    # Display the difference in earnings
    result = difference
    return result

print(solution())