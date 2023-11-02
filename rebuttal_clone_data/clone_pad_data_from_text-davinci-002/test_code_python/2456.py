def solution():
     total_raisins = 437
     raisins_first_two_boxes = 72 + 74
     raisins_in_each_of_three_remaining_boxes = (total_raisins - raisins_first_two_boxes) / 3
     result = raisins_in_each_of_three_remaining_boxes
     return result

print(solution())