def solution():
    """A convenience store sells 180 gallons of soda a week. They buy syrup boxes that can make 30 gallons of soda, and each box costs $40. How much do they pay for syrup a week?"""
    gallons_per_box = 30
    cost_per_box = 40
    boxes_per_week = 180 // gallons_per_box
    total_cost = boxes_per_week * cost_per_box
    result = total_cost
    return result

print(solution())