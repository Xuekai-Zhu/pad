def solution():
    """Abigail collected 2 boxes of cookies for the bake sale. Grayson collected 3 quarters of a box, and Olivia collected 3 boxes. Assuming that each box contains 48 cookies, how many cookies did they collect in total?"""
    # Define the number of boxes each person collected
    abigail_boxes = 2
    grayson_boxes = 0.75
    olivia_boxes = 3

    # Define the number of cookies in each box
    COOKIES_PER_BOX = 48

    # Calculate the total number of cookies collected
    total_cookies = (abigail_boxes + grayson_boxes + olivia_boxes) * COOKIES_PER_BOX

    # Display the total number of cookies collected
    result = total_cookies
    return result

print(solution())