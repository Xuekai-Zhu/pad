def solution():
    """Brian is taping up some boxes. Each box needs three pieces of tape, one as long as the long side and two as long as the short side. If Brian tapes up 5 boxes that measure 15 inches by 30 inches and 2 boxes that measure 40 inches square, how much tape does he need?"""
    # Define the number of boxes of each type
    small_boxes = 5
    large_boxes = 2

    # Define the dimensions of each box type
    small_box_dimensions = (15, 30)
    large_box_dimensions = (40, 40)

    # Define the length of tape needed for each box type
    small_box_tape = (small_box_dimensions[0] + 2 * small_box_dimensions[1])
    large_box_tape = (large_box_dimensions[0] + 2 * large_box_dimensions[1])

    # Calculate the total length of tape needed
    total_tape = small_boxes * small_box_tape + large_boxes * large_box_tape

    result = total_tape
    return result

print(solution())