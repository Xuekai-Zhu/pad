def solution():
    # Calculate the total gift wrapper available for 3 days
    total_wrapper = 90 * 3  

    # Calculate the number of gift boxes Edmund can wrap in 3 days
    gift_boxes = total_wrapper // 18  # each gift box requires 18 inches of gift wrapper
    result = gift_boxes
    return result

print(solution())