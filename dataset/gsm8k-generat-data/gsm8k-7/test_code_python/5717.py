def solution():
    abigail_boxes = 2
    grayson_boxes = 0.75
    olivia_boxes = 3
    cookies_per_box = 48

    # Calculate the total number of cookies collected
    total_cookies = (abigail_boxes + grayson_boxes + olivia_boxes) * cookies_per_box
    result = total_cookies
    return result

print(solution())