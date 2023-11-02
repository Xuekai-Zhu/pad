def solution():
    """Debbie works at a post office packing boxes to mail. Each large box takes 4 feet of packing tape to seal,
    each medium box takes 2 feet of packing tape to seal, and each small box takes 1 foot of packing tape to seal.
    Each box also takes 1 foot of packing tape to stick the address label on. Debbie packed two large boxes,
    eight medium boxes, and five small boxes this afternoon. How much tape did she use?"""
    large_tape_per_box = 4
    medium_tape_per_box = 2
    small_tape_per_box = 1
    label_tape_per_box = 1
    num_large_boxes = 2
    num_medium_boxes = 8
    num_small_boxes = 5
    total_tape = (large_tape_per_box * num_large_boxes) + (medium_tape_per_box * num_medium_boxes) + (
                small_tape_per_box * num_small_boxes) + (label_tape_per_box * (num_large_boxes + num_medium_boxes + num_small_boxes))
    result = total_tape
    return result

print(solution())