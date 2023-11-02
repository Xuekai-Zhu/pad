def solution():
    big_box_size = 7
    small_box_size = 4
    num_big_boxes = 5
    num_small_boxes = 9

    # Calculate the total number of dolls in the big boxes
    total_big_dolls = big_box_size * num_big_boxes

    # Calculate the total number of dolls in the small boxes
    total_small_dolls = small_box_size * num_small_boxes

    # Calculate the total number of dolls
    total_dolls = total_big_dolls + total_small_dolls
    result = total_dolls
    return result

print(solution())