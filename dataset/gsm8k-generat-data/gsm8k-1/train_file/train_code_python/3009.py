def solution():
    """Jon's laundry machine can do 5 pounds of laundry at a time. 4 shirts weigh 1 pound and 2 pairs of pants weigh 1 pound. If he needs to wash 20 shirts and 20 pants, how many loads of laundry does he have to do?"""
    shirts_per_load = 5 // 1 * 4
    pants_per_load = 5 // 1 * 2
    total_shirts = 20
    total_pants = 20
    total_loads = (total_shirts // shirts_per_load) + (total_pants // pants_per_load)
    result = total_loads
    return result

print(solution())