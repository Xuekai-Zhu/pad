def solution():
    # Define the number of boxes and bottles per box
    num_boxes = 10
    bottles_per_box = 50

    # Define the capacity of each bottle and the fraction filled
    bottle_capacity = 12
    fill_fraction = 3/4

    # Calculate the total volume of water in liters
    total_water_volume = num_boxes * bottles_per_box * bottle_capacity * fill_fraction

    result = total_water_volume
    return result

print(solution())