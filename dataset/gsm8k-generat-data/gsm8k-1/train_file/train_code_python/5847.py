def solution():
    """Two boxes for carrying oranges with a capacity of 80 and 50 were filled with 3/4 and 3/5 of the way full with oranges, respectively. Calculate the total number of oranges the boxes have together."""
    box1_capacity = 80
    box1_fill_percent = 0.75
    box2_capacity = 50
    box2_fill_percent = 0.6
    box1_oranges = box1_capacity * box1_fill_percent
    box2_oranges = box2_capacity * box2_fill_percent
    total_oranges = box1_oranges + box2_oranges
    result = total_oranges
    return result

print(solution())