def solution():
    loads_per_week = 3
    pods_per_load = 1
    pods_per_pack = 39
    weeks_per_year = 52

    # Calculate the total number of loads of laundry Hayes will do in a year
    total_loads_per_year = loads_per_week * weeks_per_year

    # Calculate the total number of detergent pods Hayes will need in a year
    total_pods_per_year = total_loads_per_year * pods_per_load

    # Calculate the number of packs of detergent pods Hayes will need in a year
    packs_of_pods_per_year = total_pods_per_year / pods_per_pack
    result = packs_of_pods_per_year
    return result

print(solution())