def solution():
    """A machine at the soda factory can usually fill a barrel of soda in 3 minutes. However this morning a leak went unnoticed and it took 5 minutes to fill one barrel. If the leak remains undetected, how much longer will it take to fill 12 barrels of soda than on a normal day when the machine works fine?"""
    normal_time_per_barrel = 3
    leaky_time_per_barrel = 5
    barrels_to_fill = 12
    normal_total_time = normal_time_per_barrel * barrels_to_fill
    leaky_total_time = leaky_time_per_barrel * barrels_to_fill
    extra_time = leaky_total_time - normal_total_time
    result = extra_time
    return result

print(solution())