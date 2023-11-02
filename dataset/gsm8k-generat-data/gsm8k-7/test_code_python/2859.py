def solution():
    num_boxes = 5
    box_cost = 7
    tip_percentage = 1/7
    tip_amount = (num_boxes * box_cost) * tip_percentage
    total_cost = (num_boxes * box_cost) + tip_amount
    cash_given = 100
    change = cash_given - total_cost
    result = change
    return result

print(solution())