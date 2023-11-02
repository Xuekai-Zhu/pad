def solution():
    # Calculate the number of loads of laundry Hayes does in a year
    loads_per_year = 3 * 52  # Hayes does 3 loads per week for 52 weeks in a year
    pods_per_load = 1
    pods_per_pack = 39
    packs_needed = loads_per_year * pods_per_load / pods_per_pack  # Calculate the number of packs needed
    result = packs_needed
    return result

print(solution())