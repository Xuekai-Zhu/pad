def solution():
    num_chickens_in_coop = 14
    num_chickens_in_run = num_chickens_in_coop * 2
    num_chickens_free_ranging = (num_chickens_in_run * 2) - 4
    result = num_chickens_free_ranging
    return result

print(solution())