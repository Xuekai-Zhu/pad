def solution():
    """Abigail collected 2 boxes of cookies for the bake sale. Grayson collected 3 quarters of a box, and Olivia collected 3 boxes. Assuming that each box contains 48 cookies, how many cookies did they collect in total?"""
    abigail_boxes = 2
    grayson_frac_box = 3/4
    olivia_boxes = 3
    cookies_per_box = 48
    abigail_cookies = abigail_boxes * cookies_per_box
    grayson_cookies = grayson_frac_box * cookies_per_box
    olivia_cookies = olivia_boxes * cookies_per_box
    total_cookies = abigail_cookies + grayson_cookies + olivia_cookies
    result = total_cookies
    return result

print(solution())