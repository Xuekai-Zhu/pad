def solution():
    """Spot sells cookies in bags and boxes. Each bag has 7 cookies. Each box has 12 cookies. How many more cookies are in 8 boxes than there are in 9 bags?"""
    bag_cookies = 7
    box_cookies = 12
    num_bags = 9
    num_boxes = 8
    total_cookies_in_bags = bag_cookies * num_bags
    total_cookies_in_boxes = box_cookies * num_boxes
    difference = total_cookies_in_boxes - total_cookies_in_bags
    result = difference
    return result

print(solution())