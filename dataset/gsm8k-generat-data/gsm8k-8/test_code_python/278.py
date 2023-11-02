def solution():
    # Define the square footage of the house and the barn
    house_sq_ft = 2400
    barn_sq_ft = 1000

    # Calculate the total square footage of the property
    total_sq_ft = house_sq_ft + barn_sq_ft

    # Calculate the total cost of the property
    price_per_sq_ft = 98
    total_cost = total_sq_ft * price_per_sq_ft
    result = total_cost
    return result

print(solution())