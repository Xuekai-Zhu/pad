def solution():
    """Betty is growing parsnips in her vegetable garden. When the parsnips are grown, they are harvested and bundled into boxes that can hold up to 20 parsnips each. Each harvest, three-quarters of the boxes are full, and the remaining boxes are half-full. She gets an average of 20 boxes each harvest. How many parsnips does Betty grow in an average harvest?"""
    
    # Define the maximum number of parsnips per box
    MAX_PARSNIPS_PER_BOX = 20

    # Define the fraction of boxes that are full and half-full
    FULL_BOX_FRACTION = 0.75
    HALFFULL_BOX_FRACTION = 0.25

    # Get the number of boxes per harvest
    num_boxes = 20

    # Calculate the number of parsnips in full boxes
    num_full_boxes = num_boxes * FULL_BOX_FRACTION
    num_full_parsnips = num_full_boxes * MAX_PARSNIPS_PER_BOX

    # Calculate the number of parsnips in half-full boxes
    num_halffull_boxes = num_boxes * HALFFULL_BOX_FRACTION
    num_halffull_parsnips = num_halffull_boxes * (MAX_PARSNIPS_PER_BOX / 2)

    # Calculate the total number of parsnips per harvest
    total_parsnips = num_full_parsnips + num_halffull_parsnips

    # Display the total number of parsnips per harvest
    result = total_parsnips
    return result

print(solution())