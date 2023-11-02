def solution():
    # Calculate total gift wrapper Edmund has in 3 days
    total_gift_wrapper = 90 * 3

    # Calculate the number of gift boxes Edmund can wrap with the available gift wrapper
    num_gift_boxes = total_gift_wrapper // 18
    result = num_gift_boxes
    return result

print(solution())