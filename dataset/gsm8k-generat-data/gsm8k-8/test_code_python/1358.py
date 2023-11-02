def solution():
    # Define the number of guests who want steak and chicken
    steak_guests = 3 * chicken_guests
    chicken_guests = 80 / 4

    # Calculate the cost of the steak entrees
    steak_cost = steak_guests * 25

    # Calculate the cost of the chicken entrees
    chicken_cost = chicken_guests * 18

    # Calculate the total catering budget
    total_budget = steak_cost + chicken_cost
    result = total_budget
    return result

print(solution())