def solution():
    child_1 = 3
    child_2 = 3
    child_3 = 3
    days_per_week = 5
    juice_boxes_per_day = 1
    total_juice_boxes = child_1 * days_per_week * juice_boxes_per_day + child_2 * days_per_week * juice_boxes_per_day + child_3 * days_per_week * juice_boxes_per_day
    result = total_juice_boxes
    return result

print(solution())