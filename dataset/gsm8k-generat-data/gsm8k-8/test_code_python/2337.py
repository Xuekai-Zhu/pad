def solution():
    # Calculate the total cost of each grade's shirts
    kinder_cost = 101 * 5.80
    first_cost = 113 * 5
    second_cost = 107 * 5.60
    third_cost = 108 * 5.25

    # Calculate the total cost of all the shirts
    total_cost = kinder_cost + first_cost + second_cost + third_cost
    result = total_cost
    return result

print(solution())