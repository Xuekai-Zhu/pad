def solution():
    """A restaurant has 40 tables with 4 legs and 50 tables with 3 legs. Calculate the total number of legs the restaurant's tables have."""
    num_4_leg_tables = 40
    num_3_leg_tables = 50
    legs_per_4_leg_table = 4
    legs_per_3_leg_table = 3
    total_legs = num_4_leg_tables * legs_per_4_leg_table + num_3_leg_tables * legs_per_3_leg_table
    result = total_legs
    return result

print(solution())