def solution():
    # Calculate the cost of the kitchen and bathrooms
    kitchen_cost = 20000
    bathroom_cost = 2 * 12000  # two bathrooms at 150 square feet each

    # Calculate the cost of the remaining modules
    remaining_square_feet = 2000 - 400 - 2*150
    remaining_cost = remaining_square_feet * 100

    # Calculate the total cost of the modular home
    total_cost = kitchen_cost + bathroom_cost + remaining_cost
    result = total_cost
    return result

print(solution())