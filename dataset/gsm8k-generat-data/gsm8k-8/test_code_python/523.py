def solution():
    # Define the number of loads Hayes does in a year
    loads_per_year = 3 * 52

    # Calculate the number of detergent pods needed in a year
    pods_per_load = 1
    pods_per_pack = 39
    pods_per_year = loads_per_year * pods_per_load
    packs_per_year = pods_per_year / pods_per_pack

    # Round up to the nearest whole pack
    packs_per_year = math.ceil(packs_per_year)

    result = packs_per_year
    return result

print(solution())