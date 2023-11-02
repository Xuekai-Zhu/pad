def solution():
    """A machine at the soda factory can usually fill a barrel of soda in 3 minutes. However this morning a leak went unnoticed and it took 5 minutes to fill one barrel. If the leak remains undetected, how much longer will it take to fill 12 barrels of soda than on a normal day when the machine works fine?"""
    # Define the time to fill one barrel of soda with and without the leak
    normal_time = 3
    leak_time = 5

    # Calculate the time to fill 12 barrels with and without the leak
    normal_time_12_barrels = normal_time * 12
    leak_time_12_barrels = leak_time * 12

    # Calculate the time difference
    time_difference = leak_time_12_barrels - normal_time_12_barrels

    result = time_difference
    return result

print(solution())