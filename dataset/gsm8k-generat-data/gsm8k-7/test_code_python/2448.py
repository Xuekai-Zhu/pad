def solution():
    num_boxes = 10
    bottles_per_box = 50
    bottle_capacity = 12
    fill_level = 0.75

    # Calculate the total number of bottles of water
    total_bottles = num_boxes * bottles_per_box

    # Calculate the total volume of water in liters
    total_volume = total_bottles * bottle_capacity * fill_level

    result = total_volume
    return result

print(solution())