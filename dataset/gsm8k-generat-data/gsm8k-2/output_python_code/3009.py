def solution():
    """Jon's laundry machine can do 5 pounds of laundry at a time. 4 shirts weigh 1 pound and 2 pairs of pants weigh 1 pound. If he needs to wash 20 shirts and 20 pants, how many loads of laundry does he have to do?"""
    shirts_per_load = 5 // 1
    pants_per_load = 5 // 2
    total_shirts = 20
    total_pants = 20
    total_weight = (total_shirts // 4 + total_pants // 2)
    total_loads = (total_weight + shirts_per_load - 1) // shirts_per_load
    result = total_loads
    return result

print(solution())