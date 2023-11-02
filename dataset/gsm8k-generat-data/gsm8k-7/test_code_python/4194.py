def solution():
    num_apples_in_box = 14
    num_boxes = 3
    num_apples_per_day = 2
    num_weeks = (num_apples_in_box * num_boxes) / (num_apples_per_day * 7)
    result = num_weeks
    return result

print(solution())