def solution():
    num_guests = 80

    num_steak = 3 * num_guests
    steak_cost = 25

    num_chicken = num_guests
    chicken_cost = 18

    # Calculate the total cost of all steak entrees
    total_steak_cost = num_steak * steak_cost

    # Calculate the total cost of all chicken entrees
    total_chicken_cost = num_chicken * chicken_cost

    # Calculate the total catering budget
    total_budget = total_steak_cost + total_chicken_cost
    result = total_budget
    return result

print(solution())