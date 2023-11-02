def solution():
    # Calculate the total cost of the beef
    beef_cost = 3 * 4

    # Calculate the total cost of the grocery
    total_cost = 16 - 1 - beef_cost

    # Calculate the cost of the chicken
    chicken_cost = total_cost / 2

    # Calculate the cost per person
    cost_per_person = chicken_cost / 3

    result = cost_per_person
    return result

print(solution())