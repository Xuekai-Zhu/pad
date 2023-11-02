def solution():
    large_boxes = 2
    medium_boxes = 8
    small_boxes = 5
    tape_large = large_boxes * 4
    tape_medium = medium_boxes * 2
    tape_small = small_boxes * 1
    total_tape = tape_large + tape_medium + tape_small
    result = total_tape
    return result

print(solution())