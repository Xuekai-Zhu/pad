def solution():
    
    large_box_tape = 4
    medium_box_tape = 2
    small_box_tape = 1
    address_label_tape = 1
    num_large_boxes = 2
    num_medium_boxes = 8
    num_small_boxes = 5
    total_tape = (large_box_tape * num_large_boxes) + (medium_box_tape * num_medium_boxes) + (
                small_box_tape * num_small_boxes) + ((num_large_boxes + num_medium_boxes + num_small_boxes) * address_label_tape)
    result = total_tape
    return result

print(solution())