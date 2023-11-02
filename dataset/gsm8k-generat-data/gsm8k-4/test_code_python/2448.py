def solution():
    """10 boxes each contain 50 bottles of water.  Each bottle has a capacity of 12 liters and is filled up to 3/4 of its capacity.  How many liters of water altogether are contained within the bottles in the boxes?"""
    # Define the number of boxes and bottles per box
    boxes = 10
    bottles_per_box = 50

    # Define the capacity of each bottle and the fraction of its capacity that is filled
    bottle_capacity = 12
    filled_fraction = 0.75

    # Calculate the total volume of water
    total_water = boxes * bottles_per_box * bottle_capacity * filled_fraction

    result = total_water
    return result

print(solution())