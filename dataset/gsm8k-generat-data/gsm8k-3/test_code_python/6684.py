def solution():
    """The bakery made 95 muffins. They will be packed in boxes with 5 muffins in each box. If there are only 10 available boxes, how many boxes do they still need to pack all the muffins?"""
    # Define the number of muffins and boxes
    muffins = 95
    boxes_available = 10

    # Calculate the number of boxes needed
    boxes_needed = muffins // 5

    # Calculate the number of boxes still needed
    boxes_remaining = boxes_needed - boxes_available

    # Display the number of boxes still needed
    result = boxes_remaining
    return result

print(solution())