def solution():
    """She sold twice as many boxes on Tuesday as she did on Wednesday, and she sold twice as many boxes on Wednesday as she did on Thursday. If Kim sold 1200 boxes of cupcakes on Thursday, how many boxes did she sell on Tuesday?"""
    # Define the number of boxes sold on Thursday
    thursday_boxes = 1200

    # Calculate the number of boxes sold on Wednesday
    wednesday_boxes = thursday_boxes / 2

    # Calculate the number of boxes sold on Tuesday
    tuesday_boxes = wednesday_boxes * 2

    # Display the number of boxes sold on Tuesday
    result = tuesday_boxes
    return result

print(solution())