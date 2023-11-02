def solution():
    """Spot sells cookies in bags and boxes. Each bag has 7 cookies. Each box has 12 cookies. How many more cookies are in 8 boxes than there are in 9 bags?"""
    # Define the number of cookies per bag and box
    COOKIES_PER_BAG = 7
    COOKIES_PER_BOX = 12

    # Define the number of bags and boxes
    bags = 9
    boxes = 8

    # Calculate the total number of cookies in the bags and boxes
    total_cookies_bags = bags * COOKIES_PER_BAG
    total_cookies_boxes = boxes * COOKIES_PER_BOX

    # Calculate the difference between the total number of cookies in the boxes and bags
    difference = total_cookies_boxes - total_cookies_bags

    # Display the difference
    result = difference
    return result

print(solution())