def solution():
    large_box_tape = 4  # 4 feet of packing tape to seal a large box
    medium_box_tape = 2  # 2 feet of packing tape to seal a medium box
    small_box_tape = 1  # 1 foot of packing tape to seal a small box
    label_tape = 1  # 1 foot of packing tape to stick an address label on a box

    # Calculate total tape used for large boxes
    total_large_box_tape = 2 * large_box_tape

    # Calculate total tape used for medium boxes
    total_medium_box_tape = 8 * medium_box_tape

    # Calculate total tape used for small boxes
    total_small_box_tape = 5 * small_box_tape

    # Calculate total tape used for labels
    total_label_tape = (2 + 8 + 5) * label_tape  # two large, eight medium, and five small boxes

    # Calculate total tape used for all boxes
    total_tape_used = total_large_box_tape + total_medium_box_tape + total_small_box_tape + total_label_tape
    result = total_tape_used
    return result

print(solution())