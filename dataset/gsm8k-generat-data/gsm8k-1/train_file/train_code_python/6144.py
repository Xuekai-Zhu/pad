def solution():
    """A machine at the soda factory can usually fill a barrel of soda in 3 minutes. However this morning a leak went unnoticed and it took 5 minutes to fill one barrel. If the leak remains undetected, how much longer will it take to fill 12 barrels of soda than on a normal day when the machine works fine?"""
    normal_time_per_barrel = 3
    leak_time_per_barrel = 5
    extra_time_per_barrel = leak_time_per_barrel - normal_time_per_barrel
    extra_time_to_fill_12_barrels = extra_time_per_barrel * 12
    result = extra_time_to_fill_12_barrels
    return result

print(solution())