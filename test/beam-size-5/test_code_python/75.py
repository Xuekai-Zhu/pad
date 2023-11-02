def solution():
    
    # Define the cost of the dog and the discount percentage
    DOG_COST = 100
    DISCOUNT_PERCENTAGE = 0.3

    # Calculate the discounted cost of the dog
    discounted_cost = DOG_COST - (DOG_COST * DISCOUNT_PERCENTAGE)

    # Display the discounted cost
    result = discounted_cost
    return result

print(solution())