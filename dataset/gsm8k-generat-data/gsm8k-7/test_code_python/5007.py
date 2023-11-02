def solution():
    cookies_per_bag = 7
    cookies_per_box = 12
    num_bags = 9
    num_boxes = 8

    # Calculate the total number of cookies in 9 bags
    total_cookies_in_bags = num_bags * cookies_per_bag

    # Calculate the total number of cookies in 8 boxes
    total_cookies_in_boxes = num_boxes * cookies_per_box

    # Calculate the difference in number of cookies between boxes and bags
    difference = total_cookies_in_boxes - total_cookies_in_bags
    result = difference
    return result

print(solution())