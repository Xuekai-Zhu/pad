def solution():
    big_box_dolls = 7
    small_box_dolls = 4
    num_big_boxes = 5
    num_small_boxes = 9

    # Calculate the total number of dolls in the big boxes
    total_big_box_dolls = big_box_dolls * num_big_boxes

    # Calculate the total number of dolls in the small boxes
    total_small_box_dolls = small_box_dolls * num_small_boxes

    # Calculate the total number of dolls in all the boxes
    total_dolls = total_big_box_dolls + total_small_box_dolls
    result = total_dolls
    return result

print(solution())