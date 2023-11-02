def solution():
    """10 boxes each contain 50 bottles of water. Each bottle has a capacity of 12 liters and is filled up to 3/4 of its capacity. How many liters of water altogether are contained within the bottles in the boxes?"""
    boxes = 10
    bottles_per_box = 50
    bottle_capacity = 12
    fill_percentage = 0.75
    total_liters = boxes * bottles_per_box * bottle_capacity * fill_percentage
    result = total_liters
    return result

print(solution())