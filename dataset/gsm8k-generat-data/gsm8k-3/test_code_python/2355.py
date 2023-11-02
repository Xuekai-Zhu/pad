def solution():
    """Debbie works at a post office packing boxes to mail. Each large box takes 4 feet of packing tape to seal, each medium box takes 2 feet of packing tape to seal, and each small box takes 1 foot of packing tape to seal. Each box also takes 1 foot of packing tape to stick the address label on. Debbie packed two large boxes, eight medium boxes, and five small boxes this afternoon. How much tape did she use?"""
    # Define the amount of tape for each type of box
    LARGE_BOX_TAPE = 4
    MEDIUM_BOX_TAPE = 2
    SMALL_BOX_TAPE = 1
    LABEL_TAPE = 1

    # Define the number of boxes packed
    large_boxes = 2
    medium_boxes = 8
    small_boxes = 5

    # Calculate the total amount of tape needed
    total_tape = (large_boxes * LARGE_BOX_TAPE) + (medium_boxes * MEDIUM_BOX_TAPE) + (small_boxes * SMALL_BOX_TAPE) + (large_boxes + medium_boxes + small_boxes) * LABEL_TAPE

    # Display the total amount of tape used
    result = total_tape
    return result

print(solution())