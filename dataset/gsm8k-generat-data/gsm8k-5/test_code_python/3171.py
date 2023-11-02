def solution():
    boxes_with_sides_1530 = 5  # Brian tapes up 5 boxes that measure 15 inches by 30 inches
    boxes_with_sides_4040 = 2  # Brian tapes up 2 boxes that measure 40 inches square
    tape_for_long_side = boxes_with_sides_1530 * 15 + boxes_with_sides_4040 * 40  # Total tape needed for long sides
    tape_for_short_sides = (boxes_with_sides_1530 * 2 + boxes_with_sides_4040 * 8) * 30  # Total tape needed for short sides
    total_tape_needed = tape_for_long_side + tape_for_short_sides  # Total tape needed for all boxes

    result = total_tape_needed
    return result

print(solution())