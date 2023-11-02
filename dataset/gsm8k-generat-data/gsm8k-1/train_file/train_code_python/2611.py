def solution():
    """Janet buys 45-pound containers of cat litter for $21 each. If her cat litter box holds 15 pounds of cat litter, and she changes out the litter weekly, how much will it cost, in dollars, for her to buy enough litter to last 210 days?"""
    litter_per_box = 15
    boxes_per_week = 1
    weeks_in_210_days = 210 / 7
    total_boxes = boxes_per_week * weeks_in_210_days
    cost_per_box = 21
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())