def solution():
    
    total_legs = 40
    legs_per_chair = 4
    legs_per_table = 4
    total_chairs = 6
    total_legs_used = total_chairs * legs_per_chair
    legs_remaining = total_legs - total_legs_used
    tables_with_legs = legs_remaining // legs_per_table
    result = tables_with_legs
    return result

print(solution())