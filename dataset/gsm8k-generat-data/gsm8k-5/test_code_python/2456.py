def solution():
    total_raisins = 437
    box1_raisins = 72
    box2_raisins = 74

    # Calculate total raisins in the other three boxes
    other_boxes_total = total_raisins - box1_raisins - box2_raisins

    # Divide the total raisins in the other three boxes evenly among them
    other_boxes_raisins = other_boxes_total / 3
    result = other_boxes_raisins
    return result

print(solution())