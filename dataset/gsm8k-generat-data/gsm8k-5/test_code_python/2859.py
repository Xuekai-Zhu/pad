def solution():
    number_of_boxes = 5
    cost_per_box = 7
    total_cost = number_of_boxes * cost_per_box
    tip_amount = total_cost/7
    total_amount = total_cost + tip_amount
    amount_paid = 100
    change = amount_paid - total_amount
    result = change
    return result

print(solution())