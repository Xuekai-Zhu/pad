def solution():
    total_lids = 53  # Aaron is taking 53 can lids to the recycling center
    initial_lids = 14  # Aaron already had 14 can lids
    num_boxes = 3  # Aaron used 3 equal-sized boxes of canned tomatoes
    lids_per_box = (total_lids - initial_lids) / num_boxes  # The number of can lids from each box can be calculated as the difference in total lids and initial lids, divided by the number of boxes
    result = lids_per_box
    return result

print(solution())