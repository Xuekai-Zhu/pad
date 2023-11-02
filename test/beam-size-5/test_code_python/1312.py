def solution():
    
    # Define the cost of the radiator and the discount percentage
    radiator_cost = 400
    discount_percentage = 80

    # Calculate the discounted cost of the radiator
    discounted_cost = radiator_cost * (1 - (discount_percentage / 100))

    # Calculate the cost of the mechanic
    mechanic_cost = 3 * 50

    # Calculate the total cost
    total_cost = discounted_cost + mechanic_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())