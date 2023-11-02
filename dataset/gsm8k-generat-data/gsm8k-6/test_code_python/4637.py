def solution():
    # Calculate the total amount Travis spends on cereal in a year
    boxes_per_week = 2
    cost_per_box = 3.00
    weeks_in_year = 52
    total_boxes = boxes_per_week * weeks_in_year
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())