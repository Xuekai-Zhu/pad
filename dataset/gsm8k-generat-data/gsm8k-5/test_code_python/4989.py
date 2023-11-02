def solution():
    gift_wrapper_per_box = 18  # Edmund uses 18 inches of gift wrapper per gift box
    gift_wrapper_per_day = 90  # Edmund has 90 inches of gift wrapper per day
    days = 3  # Edmund wants to know how many gift boxes he can wrap in 3 days

    # Calculate the total gift wrapper Edmund has in 3 days
    total_gift_wrapper = gift_wrapper_per_day * days

    # Calculate the number of gift boxes Edmund can wrap in 3 days
    gift_boxes = total_gift_wrapper // gift_wrapper_per_box
    result = gift_boxes
    return result

print(solution())