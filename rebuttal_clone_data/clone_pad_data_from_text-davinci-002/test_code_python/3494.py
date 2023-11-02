def solution():
    bathroom_square_feet = 24
    kitchen_square_feet = 80
    square_feet_per_minute = 8
    minutes_to_mop_bathroom = bathroom_square_feet / square_feet_per_minute
    minutes_to_mop_kitchen = kitchen_square_feet / square_feet_per_minute
    total_minutes = minutes_to_mop_bathroom + minutes_to_mop_kitchen
    result = total_minutes
    
    return result

print(solution())