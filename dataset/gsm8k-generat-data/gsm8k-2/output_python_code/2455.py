def solution():
    """Balki is counting the number of raisins in boxes of cereal. He counted 437 total raisins in 5 boxes. In one box he counted 72 raisins. In a second box he counted 74 raisins. The other three boxes had the same number each. How many were in each of the other three boxes?"""
    total_raisins = 437
    box1_raisins = 72
    box2_raisins = 74
    sum_of_other_boxes = total_raisins - box1_raisins - box2_raisins
    num_of_other_boxes = 3
    raisins_per_other_box = sum_of_other_boxes / num_of_other_boxes
    result = raisins_per_other_box
    return result

print(solution())