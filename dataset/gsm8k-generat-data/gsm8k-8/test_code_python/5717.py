def solution():
    # Define the number of boxes collected by each person
    abigail_boxes = 2
    grayson_boxes = 0.75
    olivia_boxes = 3

    # Calculate the total number of cookies collected
    total_cookies = (abigail_boxes + grayson_boxes + olivia_boxes) * 48
    result = total_cookies
    return result

print(solution())