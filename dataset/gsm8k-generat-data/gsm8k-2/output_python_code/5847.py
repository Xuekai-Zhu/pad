def solution():
    """Two boxes for carrying oranges with a capacity of 80 and 50 were filled with 3/4 and 3/5 of the way full with oranges, respectively. Calculate the total number of oranges the boxes have together."""
    
    box_1_capacity = 80
    box_1_filled = box_1_capacity * 3 / 4
    
    box_2_capacity = 50
    box_2_filled = box_2_capacity * 3 / 5
    
    total_oranges = box_1_filled + box_2_filled
    result = total_oranges
    
    return result

print(solution())