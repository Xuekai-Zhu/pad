def solution():
    num_chairs = 80
    num_tables = 20
    chair_legs = 5
    table_legs = 3
    percent_damaged = 40
    num_damaged_chairs = num_chairs * (percent_damaged / 100)
    num_damaged_tables = num_tables * (percent_damaged / 100)
    num_undamaged_chairs = num_chairs - num_damaged_chairs
    num_undamaged_tables = num_tables - num_damaged_tables
    total_legs = (num_undamaged_chairs * chair_legs) + (num_undamaged_tables * table_legs)
    result = total_legs
    return result

print(solution())