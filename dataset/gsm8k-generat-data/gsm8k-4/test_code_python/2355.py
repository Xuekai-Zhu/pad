def solution():
    """Debbie works at a post office packing boxes to mail. Each large box takes 4 feet of packing tape to seal, each medium box takes 2 feet of packing tape to seal, and each small box takes 1 foot of packing tape to seal. Each box also takes 1 foot of packing tape to stick the address label on. Debbie packed two large boxes, eight medium boxes, and five small boxes this afternoon. How much tape did she use?"""
    # Define the length of tape needed for each type of box
    LARGE_TAPE = 4
    MEDIUM_TAPE = 2
    SMALL_TAPE = 1

    # Define the number of each type of box packed
    large_boxes = 2
    medium_boxes = 8
    small_boxes = 5

    # Calculate the total length of tape used
    total_tape = (LARGE_TAPE * large_boxes) + (MEDIUM_TAPE * medium_boxes) + (SMALL_TAPE * small_boxes) + (large_boxes + medium_boxes + small_boxes)

    # return the result
    result = total_tape
    return result

print(solution())