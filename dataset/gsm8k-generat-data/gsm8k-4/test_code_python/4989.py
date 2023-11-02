def solution():
    """Edmund owns a gift wrapping shop, he uses 18 inches of gift wrapper per gift box. If Edmund has 90 inches of gift wrapper per day, how many gift boxes will he be able to wrap every 3 days?"""
    # Define the length of gift wrapper used per gift box
    WRAPPER_PER_BOX = 18

    # Define the length of gift wrapper Edmund has per day
    DAILY_WRAPPER = 90

    # Calculate the total length of gift wrapper Edmund has for 3 days
    THREE_DAY_WRAPPER = DAILY_WRAPPER * 3

    # Calculate the number of gift boxes Edmund can wrap with the available wrapper
    num_boxes = THREE_DAY_WRAPPER // WRAPPER_PER_BOX

    # return the result
    result = num_boxes
    return result

print(solution())