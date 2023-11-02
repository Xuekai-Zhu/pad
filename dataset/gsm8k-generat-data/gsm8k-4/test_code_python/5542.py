def solution():
    """Betty is growing parsnips in her vegetable garden. When the parsnips are grown, they are harvested and bundled into boxes that can hold up to 20 parsnips each. Each harvest, three-quarters of the boxes are full, and the remaining boxes are half-full. She gets an average of 20 boxes each harvest. How many parsnips does Betty grow in an average harvest?"""
    # Define the number of boxes per harvest
    boxes_per_harvest = 20

    # Calculate the number of fully-filled boxes per harvest
    full_boxes = boxes_per_harvest * 0.75

    # Calculate the number of half-filled boxes per harvest
    half_boxes = boxes_per_harvest * 0.25

    # Calculate the total number of parsnips in the fully-filled boxes
    full_box_parsnips = full_boxes * 20

    # Calculate the total number of parsnips in the half-filled boxes
    half_box_parsnips = half_boxes * 10

    # Calculate the total number of parsnips per harvest
    total_parsnips = full_box_parsnips + half_box_parsnips

    # return the result
    result = total_parsnips
    return result

print(solution())