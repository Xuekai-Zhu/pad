def solution():
    
    type_a_bricks = 40
    type_b_bricks = type_a_bricks / 2
    total_bricks_needed = 150
    bricks_of_other_types = total_bricks_needed - type_a_bricks - type_b_bricks
    result = bricks_of_other_types
    return result

print(solution())