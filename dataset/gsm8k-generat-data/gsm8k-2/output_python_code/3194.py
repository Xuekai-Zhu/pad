def solution():
    """James buys 5 packs of sodas that are 12 sodas each. He had 10 sodas already. He finishes all the sodas in 1 week. How many sodas does he drink a day?"""
    total_sodas = 5 * 12 + 10
    days = 7
    sodas_per_day = total_sodas / days
    result = sodas_per_day
    return result

print(solution())