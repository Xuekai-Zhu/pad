def solution():
    num_sodas = 3
    soda_cost = 1.0

    num_soups = 2
    soup_cost = num_sodas * soda_cost

    sandwich_cost = soup_cost * 3

    total_cost = (num_sodas * soda_cost) + (num_soups * soup_cost) + sandwich_cost

    return total_cost

print(solution())