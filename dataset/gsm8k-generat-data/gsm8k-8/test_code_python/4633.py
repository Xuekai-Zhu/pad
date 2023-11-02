def solution():
    # Calculate the total cost of their meal
    total_cost = (2 * 3.65) + 2 + 1 + 4 + (3 * 0.5) + 0.2

    # Calculate the cost per person
    per_person_cost = total_cost / 2

    # Calculate the amount of change Toby will have
    change = 15 - per_person_cost

    result = change
    return result

print(solution())