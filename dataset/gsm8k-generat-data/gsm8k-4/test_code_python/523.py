def solution():
    """Hayes does 3 loads of laundry a week using a detergent pod for each load. His detergent pods come 39 to a pack. How many packs of detergent pods will he need to do a full year of laundry?"""
    # Define the number of loads of laundry Hayes does each week and in a year
    weekly_loads = 3
    yearly_loads = weekly_loads * 52

    # Define the number of pods in a pack and calculate how many packs are needed
    pods_per_pack = 39
    packs_needed = (yearly_loads // pods_per_pack) + 1

    result = packs_needed
    return result

print(solution())