def solution():
    total_muffins = 95  # The bakery made 95 muffins
    muffins_per_box = 5  # Each box contains 5 muffins
    available_boxes = 10  # There are only 10 available boxes

    # Calculate the total number of boxes needed to pack all the muffins
    total_boxes = total_muffins // muffins_per_box

    # Calculate the number of boxes still needed
    boxes_needed = total_boxes - available_boxes
    result = boxes_needed
    return result

print(solution())