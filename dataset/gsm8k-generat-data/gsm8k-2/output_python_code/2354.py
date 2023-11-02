def solution():
    """Debbie works at a post office packing boxes to mail. Each large box takes 4 feet of packing tape to seal, each medium box takes 2 feet of packing tape to seal, and each small box takes 1 foot of packing tape to seal. Each box also takes 1 foot of packing tape to stick the address label on. Debbie packed two large boxes, eight medium boxes, and five small boxes this afternoon. How much tape did she use?"""
    large_box_tape = 4
    medium_box_tape = 2
    small_box_tape = 1
    address_label_tape = 1
    num_large_boxes = 2
    num_medium_boxes = 8
    num_small_boxes = 5
    total_tape = (large_box_tape * num_large_boxes) + (medium_box_tape * num_medium_boxes) + (
                small_box_tape * num_small_boxes) + ((num_large_boxes + num_medium_boxes + num_small_boxes) * address_label_tape)
    result = total_tape
    return result

print(solution())