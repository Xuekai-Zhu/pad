def solution():
    # Calculate the total cost of the first half of the season
    first_half_cost = 1000 * (22/2)

    # Calculate the total cost of the second half of the season
    second_half_cost = 1.2 * 1000 * (22/2)

    # Calculate the total cost of the entire season
    total_cost = first_half_cost + second_half_cost
    result = total_cost
    return result

print(solution())