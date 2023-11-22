def solution():
    
    # Define the cost of the dog and the discount percentage
    dog_cost = 100
    discount_percentage = 0.3

    # Calculate the discounted cost of the dog
    discounted_cost = dog_cost * (1 - discount_percentage)

    # Return the final cost of the grooming
    result = discounted_cost
    return result

print(solution())