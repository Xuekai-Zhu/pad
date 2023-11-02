def solution():
    """Madeline has 5 boxes with 24 crayons in each. She noticed that 5/8 of the crayons in the 2 boxes were not yet used. In the 2 other boxes, only 2/3 of the crayons were used while the last box was not entirely used. How many unused crayons did Madeline have?"""
    boxes_total = 5
    crayons_per_box = 24

    # first two boxes
    unused_1 = (5/8) * crayons_per_box
    unused_2 = (5/8) * crayons_per_box
    total_unused_1_2 = unused_1 + unused_2

    # next two boxes
    used_1 = (2/3) * crayons_per_box
    used_2 = (2/3) * crayons_per_box
    total_unused_3_4 = (crayons_per_box - used_1) + (crayons_per_box - used_2)

    # last box
    unused_5 = crayons_per_box - 8
    total_unused = total_unused_1_2 + total_unused_3_4 + unused_5

    result = total_unused
    return result

print(solution())