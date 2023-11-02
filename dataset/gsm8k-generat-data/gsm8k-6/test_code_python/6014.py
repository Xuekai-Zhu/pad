def solution():
    soda_cost = 1
    soup_cost = 3 * soda_cost  # each soup costs as much as 3 sodas
    sandwich_cost = 3 * soup_cost  # the sandwich costs 3 times as much as 1 soup
    total_cost = (3 * soda_cost) + (2 * soup_cost) + sandwich_cost  # total cost of the items
    result = total_cost
    return result

print(solution())