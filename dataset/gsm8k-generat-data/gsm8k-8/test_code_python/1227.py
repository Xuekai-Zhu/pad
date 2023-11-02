def solution():
    # Calculate the total number of loose crayons
    total_loose_crayons = 5 + 27

    # Calculate the total number of crayons in the full boxes
    total_full_boxes = 5 * 24

    # Calculate the total number of crayons
    total_crayons = total_loose_crayons + total_full_boxes

    # Calculate the number of boxes needed for all the crayons
    boxes_needed = (total_crayons - 85) // 24 + 1

    result = boxes_needed
    return result

print(solution())