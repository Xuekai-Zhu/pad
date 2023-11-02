def solution():
    """Jack needs to mop the bathroom and the kitchen. If the bathroom floor is 24 square feet and the kitchen floor is 80 square feet, and Jack can mop 8 square feet per minute, how many minutes does he spend mopping?"""
    bathroom_size = 24
    kitchen_size = 80
    total_size = bathroom_size + kitchen_size
    mopping_speed = 8
    total_mopping_time = total_size / mopping_speed
    result = total_mopping_time
    return result

print(solution())