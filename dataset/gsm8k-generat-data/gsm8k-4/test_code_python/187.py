def solution():
    """Madeline has 5 boxes with 24 crayons in each. She noticed that 5/8 of the crayons in the 2 boxes were not yet used. In the 2 other boxes, only 2/3 of the crayons were used while the last box was not entirely used. How many unused crayons did Madeline have?"""
    # Define the number of boxes and crayons per box
    boxes = 5
    crayons_per_box = 24

    # Calculate the number of crayons in all the boxes
    total_crayons = boxes * crayons_per_box

    # Calculate the number of unused crayons in the first two boxes
    unused_crayons_box1 = (5/8) * crayons_per_box
    unused_crayons_box2 = (5/8) * crayons_per_box
    total_unused1 = unused_crayons_box1 + unused_crayons_box2

    # Calculate the number of used crayons in the two other boxes
    used_crayons_box1 = (1 - 2/3) * crayons_per_box
    used_crayons_box2 = (1 - 2/3) * crayons_per_box
    total_unused2 = used_crayons_box1 + used_crayons_box2

    # Calculate the number of unused crayons in the last box
    unused_crayons_box3 = crayons_per_box - total_unused2

    # Calculate the total number of unused crayons
    total_unused = total_unused1 + unused_crayons_box3

    # return the result
    result = total_unused
    return result

print(solution())