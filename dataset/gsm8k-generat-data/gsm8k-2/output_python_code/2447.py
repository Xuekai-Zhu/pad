def solution():
    """10 boxes each contain 50 bottles of water. Each bottle has a capacity of 12 liters and is filled up to 3/4 of its capacity. How many liters of water altogether are contained within the bottles in the boxes?"""
    box_count = 10
    bottle_count = 50
    bottle_capacity = 12
    fill_ratio = 3/4
    total_liters = box_count * bottle_count * bottle_capacity * fill_ratio
    result = total_liters
    return result

print(solution())