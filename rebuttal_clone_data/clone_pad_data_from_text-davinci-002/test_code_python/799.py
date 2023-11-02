def solution():
    four_legged_tables = 4
    three_legged_tables = 3
    one_legged_table = 1
    two_legged_chair = 1
    four_legged_chairs = 2
    legs_per_four_legged_table = 4
    legs_per_three_legged_table = 3
    legs_per_one_legged_table = 1
    legs_per_two_legged_chair = 2
    legs_per_four_legged_chair = 4
    total_legs = (four_legged_tables * legs_per_four_legged_table) + (three_legged_tables * legs_per_three_legged_table) + (one_legged_table * legs_per_one_legged_table) + (two_legged_chair * legs_per_two_legged_chair) + (four_legged_chairs * legs_per_four_legged_chair)
    result = total_legs
    
    return result

print(solution())