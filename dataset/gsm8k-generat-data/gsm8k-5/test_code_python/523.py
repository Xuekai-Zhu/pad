def solution():
    loads_per_week = 3  # Hayes does 3 loads of laundry a week
    pods_per_load = 1  # Hayes uses 1 detergent pod per load
    pods_per_pack = 39  # There are 39 detergent pods in a pack
    weeks_per_year = 52  # There are 52 weeks in a year

    # Calculate the total number of detergent pods Hayes will need for the year
    total_pods = loads_per_week * pods_per_load * weeks_per_year

    # Calculate the number of packs of detergent pods Hayes will need
    packs_of_pods = (total_pods + (pods_per_pack - 1)) // pods_per_pack  # Round up to the nearest pack
    result = packs_of_pods
    return result

print(solution())