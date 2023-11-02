def solution():
    num_tissues_per_box = 160
    num_boxes = 3
    num_used_tissues = 210

    # Calculate the total number of tissues Tucker had at the start
    total_tissues_at_start = num_tissues_per_box * num_boxes

    # Calculate the number of tissues Tucker has left after using some
    num_tissues_left = total_tissues_at_start - num_used_tissues
    result = num_tissues_left
    return result

print(solution())