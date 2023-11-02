def solution():
    """Edmund owns a gift wrapping shop, he uses 18 inches of gift wrapper per gift box. If Edmund has 90 inches of gift wrapper per day, how many gift boxes will he be able to wrap every 3 days?"""
    # Calculate the total gift wrapper Edmund has in 3 days
    total_wrapper = 90 * 3

    # Calculate the number of gift boxes Edmund can wrap with the total wrapper
    num_boxes = total_wrapper // 18

    # Display the number of gift boxes Edmund can wrap every 3 days
    result = num_boxes
    return result

print(solution())