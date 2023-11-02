def solution():
    """Zach rented a car for $150 plus 50 cents for each mile. He drove 620 miles on Monday and another 744 miles on Thursday. How much did he spend?"""
    # Define the rental cost and cost per mile
    RENTAL_COST = 150
    COST_PER_MILE = 0.5

    # Calculate the total distance traveled
    total_distance = 620 + 744

    # Calculate the total cost
    total_cost = RENTAL_COST + total_distance * COST_PER_MILE

    # Display the total cost
    result = total_cost
    return result

print(solution())