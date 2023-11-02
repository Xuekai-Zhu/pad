def solution():
    """Aaron is gathering can lids to take to the recycling center. He uses 3 equal-sized boxes of canned tomatoes and adds the lids he gets to the 14 can lids he already has. He is now taking 53 can lids to the recycling center. How many cans lids did he get from each box?"""
    # Define the number of can lids Aaron had before
    starting_lids = 14

    # Define the total number of can lids Aaron has now
    total_lids = 53

    # Define the number of boxes of canned tomatoes Aaron used
    num_boxes = 3

    # Calculate the number of can lids Aaron got from each box
    lids_per_box = (total_lids - starting_lids) / num_boxes

    # Display the number of can lids per box
    result = lids_per_box
    return result

print(solution())