def solution():
    boxes_per_week = 2
    cost_per_box = 3.0
    num_weeks = 52
    num_boxes = boxes_per_week * num_weeks

    # Calculate the total cost of all cereal boxes
    total_cost = num_boxes * cost_per_box
    result = total_cost
    return result

print(solution())