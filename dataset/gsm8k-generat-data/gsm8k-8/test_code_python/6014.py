def solution():
    soda_cost = 1
    soup_cost = 3 * soda_cost
    sandwich_cost = 3 * soup_cost

    total_cost = 3 * soda_cost + 2 * soup_cost + sandwich_cost
    result = total_cost
    return result

print(solution())