def solution():
    total_cans = 24
    orange_pop_ratio = 2

    # Calculate the total number of cherry soda cans
    cherry_soda_cans = total_cans / (1 + orange_pop_ratio)

    result = cherry_soda_cans
    return result

print(solution())