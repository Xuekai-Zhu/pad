def solution():
    # Define the variables
    rental_budget = 0
    food_budget = 0
    phone_budget = 0
    total_budget = 0

    # Calculate the rental budget
    rental_budget = 240 * (1 - 0.6)

    # Calculate the food budget
    food_budget = 240 * 0.6

    # Calculate the phone budget
    phone_budget = food_budget * 0.1

    # Calculate the total budget
    total_budget = rental_budget + food_budget + phone_budget
    result = total_budget
    return result

print(solution())