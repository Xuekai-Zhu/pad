def solution():
    """10 boxes each contain 50 bottles of water.  Each bottle has a capacity of 12 liters and is filled up to 3/4 of its capacity.  How many liters of water altogether are contained within the bottles in the boxes?"""
    # Define the number of boxes and bottles per box
    NUM_BOXES = 10
    BOTTLES_PER_BOX = 50

    # Define the capacity of each bottle and the fraction filled
    BOTTLE_CAPACITY = 12
    FRACTION_FILLED = 3/4

    # Calculate the total volume of water
    total_water = NUM_BOXES * BOTTLES_PER_BOX * BOTTLE_CAPACITY * FRACTION_FILLED

    # Display the total volume of water
    result = total_water
    return result

print(solution())