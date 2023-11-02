def solution():
    

    
    chairs = 80
    legs_per_chair = 5
    total_legs_chairs = chairs * legs_per_chair

    
    tables = 20
    legs_per_table = 3
    total_legs_tables = tables * legs_per_table

    
    damaged_chairs = 0.4 * chairs
    remaining_chairs = chairs - damaged_chairs

    
    total_legs = (remaining_chairs * legs_per_chair) + total_legs_tables

    result = total_legs
    return result

print(solution())