def solution():
    # Calculate the total tape in feet used by Debbie
    tape_large_boxes = 4 * 2  # two large boxes each take 4 feet of tape to seal
    tape_medium_boxes = 2 * 8  # eight medium boxes each take 2 feet of tape to seal
    tape_small_boxes = 1 * 5  # five small boxes each take 1 foot of tape to seal
    tape_address_label = 1 * 15  # each box requires 1 foot of tape to stick the address label on
    total_tape = tape_large_boxes + tape_medium_boxes + tape_small_boxes + tape_address_label
    
    result = total_tape
    return result

print(solution())