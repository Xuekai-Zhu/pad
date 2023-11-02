def solution():
    """Francine has five full boxes of crayons and 5 loose crayons, and her friend has 27 loose crayons. They need to put all of their loose crayons in a box. How many more boxes do they need if Francine has a total of 85 crayons?"""
    # Define the total number of crayons
    total_crayons = 85

    # Calculate the number of crayons in the boxes
    box_crayons = 5 * 24

    # Calculate the total number of loose crayons
    loose_crayons = total_crayons - box_crayons

    # Calculate the total number of boxes needed
    boxes_needed = (loose_crayons + 27 + 23) // 24

    # Calculate the number of additional boxes needed
    additional_boxes = boxes_needed - 5

    # return the result
    result = additional_boxes
    return result

print(solution())