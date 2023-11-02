def solution():
    """Aaron is gathering can lids to take to the recycling center. He uses 3 equal-sized boxes of canned tomatoes and adds the lids he gets to the 14 can lids he already has. He is now taking 53 can lids to the recycling center. How many cans lids did he get from each box?"""
    # Define the initial number of can lids and the number of boxes
    initial_lids = 14
    num_boxes = 3

    # Calculate the total number of can lids including those in the boxes
    total_lids = initial_lids + 53

    # Calculate the number of can lids per box
    lids_per_box = total_lids / num_boxes

    result = lids_per_box - initial_lids/num_boxes
    return result

print(solution())