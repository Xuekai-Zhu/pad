def solution():
    total_can_lids = 53
    initial_can_lids = 14
    num_boxes = 3

    # Calculate the number of can lids Aaron got from the boxes of canned tomatoes
    can_lids_from_boxes = total_can_lids - initial_can_lids

    # Calculate the number of can lids per box of canned tomatoes
    can_lids_per_box = can_lids_from_boxes / num_boxes
    result = can_lids_per_box
    return result

print(solution())