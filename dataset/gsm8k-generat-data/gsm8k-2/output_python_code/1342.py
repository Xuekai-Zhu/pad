def solution():
    """There are 1250 pairs of shoes in the warehouse. There are 540 pairs that are blue. The rest are either green or purple. The number of green shoes is equal to the number of purple shoes. How many pairs of purple shoes are in the warehouse?"""
    total_shoes = 1250
    blue_shoes = 540
    green_shoes = (total_shoes - blue_shoes) / 2
    purple_shoes = green_shoes
    result = purple_shoes
    return result

print(solution())