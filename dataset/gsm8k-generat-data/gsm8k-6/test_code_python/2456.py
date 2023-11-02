def solution():
    # Calculate the total number of raisins in the five boxes
    total_raisins = 437

    # Calculate the number of raisins in the first two boxes
    raisins_first_two_boxes = 72 + 74

    # Calculate the number of raisins in the other three boxes
    raisins_other_boxes = (total_raisins - raisins_first_two_boxes) / 3

    result = raisins_other_boxes
    return result

print(solution())