def solution():
    """Spot sells cookies in bags and boxes. Each bag has 7 cookies. Each box has 12 cookies. How many more cookies are in 8 boxes than there are in 9 bags?"""
    # Define the number of cookies in each bag and box
    COOKIES_PER_BAG = 7
    COOKIES_PER_BOX = 12

    # Calculate the total number of cookies in 8 boxes
    cookies_in_boxes = 8 * COOKIES_PER_BOX

    # Calculate the total number of cookies in 9 bags
    cookies_in_bags = 9 * COOKIES_PER_BAG

    # Calculate the difference in the number of cookies
    difference = cookies_in_boxes - cookies_in_bags

    # Display the result
    result = difference
    return result

print(solution())