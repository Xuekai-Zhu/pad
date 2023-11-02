def solution():
    # Calculate the total weight of all 12 eggs
    total_weight = 12 * 10

    # Calculate the number of eggs in each of the remaining 3 boxes
    remaining_boxes = 3
    eggs_per_box = 12 // remaining_boxes

    # Calculate the total weight of the remaining eggs
    remaining_weight = eggs_per_box * 10 * remaining_boxes
    
    result = remaining_weight
    return result

print(solution())