def solution():
    # Calculate the number of can lids Aaron got from each box
    num_boxes = 3
    total_lids = 53
    initial_lids = 14
    lids_per_box = (total_lids - initial_lids) / num_boxes
    result = lids_per_box
    return result

print(solution())