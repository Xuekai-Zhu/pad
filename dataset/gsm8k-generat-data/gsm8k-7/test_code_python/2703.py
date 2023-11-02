def solution():
    orange_boxes = 6
    orange_per_box = 8

    blue_boxes = 7
    blue_per_box = 5

    red_box = 1
    red_per_box = 11

    # Calculate total number of orange crayons
    total_orange = orange_boxes * orange_per_box

    # Calculate total number of blue crayons
    total_blue = blue_boxes * blue_per_box

    # Calculate total number of red crayons
    total_red = red_box * red_per_box

    # Calculate total number of crayons
    total_crayons = total_orange + total_blue + total_red
    result = total_crayons
    return result

print(solution())