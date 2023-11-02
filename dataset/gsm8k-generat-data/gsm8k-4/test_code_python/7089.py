def solution():
    """Zach rented a car for $150 plus 50 cents for each mile. He drove 620 miles on Monday and another 744 miles on Thursday. How much did he spend?"""
    # Define the rental cost and the cost per mile
    rental_cost = 150
    cost_per_mile = 0.5

    # Calculate the total miles driven
    total_miles = 620 + 744

    # Calculate the total cost
    total_cost = rental_cost + total_miles * cost_per_mile

    # Return the result
    result = total_cost
    return result

print(solution())