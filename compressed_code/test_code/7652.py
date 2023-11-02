def solution():
    
    large_tape_per_box = 4
    medium_tape_per_box = 2
    small_tape_per_box = 1
    label_tape_per_box = 1
    num_large_boxes = 2
    num_medium_boxes = 8
    num_small_boxes = 5
    total_tape = (large_tape_per_box * num_large_boxes) + (medium_tape_per_box * num_medium_boxes) + (
                small_tape_per_box * num_small_boxes) + (label_tape_per_box * (num_large_boxes + num_medium_boxes + num_small_boxes))
    result = total_tape
    return result

print(solution())