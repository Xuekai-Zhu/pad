def solution():
    """Francine has five full boxes of crayons and 5 loose crayons, and her friend has 27 loose crayons.
    They need to put all of their loose crayons in a box. How many more boxes do they need if Francine has a total of 85 crayons?"""
    # Define the total number of crayons Francine and her friend have
    total_crayons = 85 + 27

    # Define the number of crayons a box can hold
    BOX_CAPACITY = 24

    # Calculate the total number of boxes needed to hold all the loose crayons
    loose_crayons_boxes = (total_crayons - 5 * 5) // BOX_CAPACITY + 1

    # Calculate the number of boxes Francine already has
    full_boxes = 5

    # Calculate the number of additional boxes needed
    additional_boxes = loose_crayons_boxes - full_boxes

    # Display the number of additional boxes needed
    result = additional_boxes
    return result

print(solution())