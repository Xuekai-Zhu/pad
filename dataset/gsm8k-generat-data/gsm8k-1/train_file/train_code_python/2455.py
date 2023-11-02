def solution():
    """Balki is counting the number of raisins in boxes of cereal. He counted 437 total raisins in 5 boxes. In one box he counted 72 raisins. In a second box he counted 74 raisins. The other three boxes had the same number each. How many were in each of the other three boxes?"""
    total_raisins = 437
    known_raisins = 72 + 74
    unknown_raisins = total_raisins - known_raisins
    num_other_boxes = 3
    raisins_per_box = unknown_raisins / num_other_boxes
    result = raisins_per_box
    return result

print(solution())