def solution():
    num_boxes = 5
    crayons_per_box = 24
    num_loose_crayons_francine = 5
    num_loose_crayons_friend = 27
    total_crayons = 85

    # Calculate the total number of crayons Francine has in her boxes
    total_boxes_crayons = num_boxes * crayons_per_box

    # Calculate the total number of loose crayons Francine has
    total_loose_crayons_francine = num_loose_crayons_francine

    # Calculate the total number of loose crayons her friend has
    total_loose_crayons_friend = num_loose_crayons_friend

    # Calculate the total number of loose crayons they have together
    total_loose_crayons = total_loose_crayons_francine + total_loose_crayons_friend

    # Calculate the total number of boxes needed to store all the loose crayons
    num_boxes_needed = (total_crayons - total_boxes_crayons - total_loose_crayons) / crayons_per_box

    result = num_boxes_needed
    return result

print(solution())