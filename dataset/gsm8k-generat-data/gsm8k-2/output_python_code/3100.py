def solution():
    """A convenience store sells 180  gallons of soda a week. They buy syrup boxes that can make 30 gallons of soda, and each box costs $40. How much do they pay for syrup a week?"""
    soda_per_box = 30
    price_per_box = 40
    total_boxes_needed = 180 / soda_per_box
    total_cost = total_boxes_needed * price_per_box
    result = total_cost
    return result

print(solution())