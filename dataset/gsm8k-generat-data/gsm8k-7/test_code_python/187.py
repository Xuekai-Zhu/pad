def solution():
    num_boxes = 5
    crayons_per_box = 24

    # Calculate the total number of crayons
    total_crayons = num_boxes * crayons_per_box

    # Calculate the number of unused crayons in the first two boxes
    unused_crayons_first_two_boxes = (5/8) * (2 * crayons_per_box)

    # Calculate the number of used crayons in the third and fourth boxes
    used_crayons_third_fourth_boxes = (1 - (2/3)) * (2 * crayons_per_box)

    # Calculate the number of unused crayons in the last box
    unused_crayons_last_box = crayons_per_box - used_crayons_third_fourth_boxes

    # Calculate the total number of unused crayons
    total_unused_crayons = unused_crayons_first_two_boxes + unused_crayons_last_box

    result = total_unused_crayons
    return result

print(solution())