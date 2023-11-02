def solution():
    """Abigail collected 2 boxes of cookies for the bake sale. Grayson collected 3 quarters of a box, and Olivia collected 3 boxes. Assuming that each box contains 48 cookies, how many cookies did they collect in total?"""
    abigail_boxes = 2
    grayson_boxes = 0.75
    olivia_boxes = 3
    cookies_per_box = 48
    total_cookies = (abigail_boxes + grayson_boxes + olivia_boxes) * cookies_per_box
    result = total_cookies
    return result

print(solution())