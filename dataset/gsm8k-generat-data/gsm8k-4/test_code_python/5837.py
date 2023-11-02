def solution():
    """Harold's fancy wrapping paper can wrap 5 shirt boxes or 3 XL boxes. 
    For the upcoming holiday, he has 20 shirt boxes to wrap and 12 XL boxes to wrap. 
    If each roll of wrapping paper costs $4.00 per roll, how much will he spend to wrap all of the boxes?"""
    # Define the number of boxes that can be wrapped with one roll of wrapping paper
    shirt_boxes_per_roll = 5
    xl_boxes_per_roll = 3

    # Calculate the number of rolls needed to wrap all the shirt boxes
    shirt_rolls = (20 + shirt_boxes_per_roll - 1) // shirt_boxes_per_roll

    # Calculate the number of rolls needed to wrap all the XL boxes
    xl_rolls = (12 + xl_boxes_per_roll - 1) // xl_boxes_per_roll

    # Calculate the total number of rolls needed
    total_rolls = shirt_rolls + xl_rolls

    # Calculate the total cost of the rolls needed
    total_cost = total_rolls * 4

    # Return the result
    result = total_cost
    return result

print(solution())