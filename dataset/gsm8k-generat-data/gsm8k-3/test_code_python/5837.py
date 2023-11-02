def solution():
    """Harold's fancy wrapping paper can wrap 5 shirt boxes or 3 XL boxes.  For the upcoming holiday, he has 20 shirt boxes to wrap and 12 XL boxes to wrap.  If each roll of wrapping paper costs $4.00 per roll, how much will he spend to wrap all of the boxes?"""
    # Define the number of boxes that can be wrapped per roll of wrapping paper
    SHIRT_BOXES_PER_ROLL = 5
    XL_BOXES_PER_ROLL = 3

    # Define the number of boxes to be wrapped
    shirt_boxes = 20
    xl_boxes = 12

    # Calculate the total number of rolls of wrapping paper needed for the shirt boxes
    shirt_rolls = shirt_boxes // SHIRT_BOXES_PER_ROLL
    if shirt_boxes % SHIRT_BOXES_PER_ROLL != 0:
        shirt_rolls += 1

    # Calculate the total number of rolls of wrapping paper needed for the XL boxes
    xl_rolls = xl_boxes // XL_BOXES_PER_ROLL
    if xl_boxes % XL_BOXES_PER_ROLL != 0:
        xl_rolls += 1

    # Calculate the total number of rolls of wrapping paper needed
    total_rolls = shirt_rolls + xl_rolls

    # Calculate the total cost of the wrapping paper
    total_cost = total_rolls * 4

    # Display the total cost
    result = total_cost
    return result

print(solution())