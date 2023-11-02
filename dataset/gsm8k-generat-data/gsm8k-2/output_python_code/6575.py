def solution():
    """Aaron is gathering can lids to take to the recycling center. He uses 3 equal-sized boxes of canned tomatoes and adds the lids he gets to the 14 can lids he already has. He is now taking 53 can lids to the recycling center. How many cans lids did he get from each box?"""
    total_lids = 53
    initial_lids = 14
    lids_per_box = (total_lids - initial_lids) / 3
    result = lids_per_box
    return result

print(solution())