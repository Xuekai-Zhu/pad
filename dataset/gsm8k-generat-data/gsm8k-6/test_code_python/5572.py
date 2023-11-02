def solution():
    # Calculate the total number of presents Alicia got for her birthday
    small_boxes = 10  # number of presents in small boxes
    medium_boxes = 12  # number of presents in medium boxes
    large_boxes = (small_boxes + medium_boxes) / 3  # number of presents in large boxes (1/3 of total)
    total_presents = small_boxes + medium_boxes + large_boxes
    result = total_presents
    return result

print(solution())