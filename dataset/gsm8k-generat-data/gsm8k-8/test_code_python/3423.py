def solution():
    chickens_in_coop = 14
    chickens_in_run = 2 * chickens_in_coop
    chickens_free_ranging = 2 * chickens_in_run - 4
    result = chickens_free_ranging
    return result

print(solution())