def solution():
    """Madeline has 5 boxes with 24 crayons in each. She noticed that 5/8 of the crayons in the 2 boxes were not yet used.
    In the 2 other boxes, only 2/3 of the crayons were used while the last box was not entirely used. How many unused crayons did Madeline have?"""
    # Define the total number of boxes and crayons per box
    total_boxes = 5
    crayons_per_box = 24

    # Calculate the number of unused crayons in the first two boxes
    unused_crayons_1 = (5/8) * crayons_per_box * 2

    # Calculate the number of used crayons in the other two boxes
    used_crayons_2 = (2/3) * crayons_per_box * 2

    # Calculate the number of unused crayons in the last box
    unused_crayons_3 = crayons_per_box - used_crayons_2

    # Calculate the total number of unused crayons
    total_unused_crayons = unused_crayons_1 + unused_crayons_3

    # return the result
    result = total_unused_crayons
    return result

print(solution())