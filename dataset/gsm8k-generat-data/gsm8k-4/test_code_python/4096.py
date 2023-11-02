def solution():
    """Mrs. Thompson bought 3 chickens for $3 each. She also bought a bag of potatoes. Mrs. Thompson paid $15 in total. How much did the potatoes cost?"""
    # Define the cost of each chicken and the total cost of the chickens
    CHICKEN_COST = 3
    TOTAL_CHICKEN_COST = CHICKEN_COST * 3

    # Define the total cost paid by Mrs. Thompson
    TOTAL_COST = 15

    # Calculate the cost of the potatoes
    POTATOES_COST = TOTAL_COST - TOTAL_CHICKEN_COST

    # return the cost of the potatoes
    result = POTATOES_COST
    return result

print(solution())