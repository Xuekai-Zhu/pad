def solution():
    """Hayes does 3 loads of laundry a week using a detergent pod for each load. His detergent pods come 39 to a pack. How many packs of detergent pods will he need to do a full year of laundry?"""
    loads_per_week = 3
    pods_per_load = 1
    pods_per_pack = 39
    weeks_per_year = 52
    total_loads = loads_per_week * weeks_per_year
    total_pods = total_loads * pods_per_load
    packs_needed = total_pods // pods_per_pack + (total_pods % pods_per_pack > 0)
    result = packs_needed
    return result

print(solution())