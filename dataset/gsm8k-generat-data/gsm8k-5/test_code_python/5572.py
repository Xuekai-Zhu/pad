def solution():
    # Calculate the total number of presents in small and medium boxes
    small_boxes = 10
    medium_boxes = 12
    total_small_medium = small_boxes + medium_boxes

    # Calculate the total number of presents in large boxes
    total_gifts = total_small_medium / (1/3)

    # Calculate the total number of presents Alicia got for her birthday
    total_presents = total_small_medium + total_gifts
    result = total_presents
    return result

print(solution())