def solution():
    num_boxes_15_30 = 5
    num_boxes_40 = 2

    # Calculate the length of tape needed for boxes that measure 15 inches by 30 inches
    length_tape_15_30 = (15 + 30) * 2 + (15 * 2) * num_boxes_15_30

    # Calculate the length of tape needed for boxes that measure 40 inches square
    length_tape_40 = (40 * 2) + (40 * 2 * 2) * num_boxes_40

    # Calculate the total length of tape needed
    total_length_tape = length_tape_15_30 + length_tape_40
    result = total_length_tape
    return result

print(solution())