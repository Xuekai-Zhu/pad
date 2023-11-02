def solution():
    """Jack needs to mop the bathroom and the kitchen. If the bathroom floor is 24 square feet and the kitchen floor is 80 square feet, and Jack can mop 8 square feet per minute, how many minutes does he spend mopping?"""
    bathroom_area = 24
    kitchen_area = 80
    total_area = bathroom_area + kitchen_area
    mopping_rate = 8
    minutes_spent_mopping = total_area / mopping_rate
    result = minutes_spent_mopping
    return result

print(solution())