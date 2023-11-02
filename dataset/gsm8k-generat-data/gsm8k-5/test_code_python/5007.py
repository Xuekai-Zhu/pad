def solution():
    cookies_per_bag = 7  # Each bag has 7 cookies
    cookies_per_box = 12  # Each box has 12 cookies
    num_boxes = 8  # Spot has 8 boxes
    num_bags = 9  # Spot has 9 bags

    # Calculate the total number of cookies in the boxes
    total_cookies_in_boxes = cookies_per_box * num_boxes

    # Calculate the total number of cookies in the bags
    total_cookies_in_bags = cookies_per_bag * num_bags

    # Calculate the difference in the number of cookies
    difference = total_cookies_in_boxes - total_cookies_in_bags
    result = difference
    return result

print(solution())