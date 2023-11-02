def solution():
    """The bakery made 95 muffins. They will be packed in boxes with 5 muffins in each box. If there are only 10 available boxes, how many boxes do they still need to pack all the muffins?"""
    # Define the number of muffins and muffins per box
    total_muffins = 95
    muffins_per_box = 5

    # Calculate the number of boxes needed to pack all the muffins
    total_boxes = total_muffins // muffins_per_box

    # Calculate the number of remaining muffins after packing all the boxes
    remaining_muffins = total_muffins % muffins_per_box

    # Calculate the number of boxes needed to pack the remaining muffins
    if remaining_muffins > 0:
        remaining_boxes = 1
    else:
        remaining_boxes = 0

    # Calculate the total number of boxes needed
    total_boxes += remaining_boxes

    # Calculate the number of boxes still needed
    boxes_needed = total_boxes - 10

    result = boxes_needed
    return result

print(solution())