def solution():
    # Calculate the total number of raisins in 5 boxes
    total_raisins = 437

    # Subtract the number of raisins in the first two boxes
    remaining_raisins = total_raisins - 72 - 74

    # Divide the remaining raisins equally among the three boxes
    num_other_boxes = 3
    raisins_per_box = remaining_raisins / num_other_boxes

    result = raisins_per_box
    return result

print(solution())