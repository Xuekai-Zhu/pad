def solution():
    """Travis goes through 2 boxes of cereal a week. If each box costs $3.00 and he eats 2 boxes every week for an entire year, 52 weeks, how much does he spend on cereal?"""
    boxes_per_week = 2
    cost_per_box = 3.00
    weeks_per_year = 52
    total_boxes = boxes_per_week * weeks_per_year
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())