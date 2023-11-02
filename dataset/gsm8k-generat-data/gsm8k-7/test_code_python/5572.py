def solution():
    num_small_boxes = 10
    num_medium_boxes = 12
    total_boxes = num_small_boxes + num_medium_boxes

    # Calculate the total number of presents in large boxes
    num_large_boxes = total_boxes / 3
    total_presents = num_small_boxes + num_medium_boxes + num_large_boxes
    result = total_presents
    return result

print(solution())