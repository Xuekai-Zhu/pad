def solution():
    # Calculate the total cost of the oysters
    oyster_cost = 3 * 15

    # Calculate the total cost of the shrimp
    shrimp_cost = 2 * 14

    # Calculate the total cost of the clams
    clam_cost = 2 * 13.5

    # Calculate the total cost of the meal
    total_cost = oyster_cost + shrimp_cost + clam_cost

    # Calculate the cost per person
    cost_per_person = total_cost / 4
    result = cost_per_person
    return result

print(solution())