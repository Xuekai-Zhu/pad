def solution():
    """There is a very large room that has 4 tables, 1 sofa and 2 chairs that have 4 legs each. There are also 3 tables with 3 legs each, 1 table with 1 leg, and 1 rocking chair with 2 legs. How many legs are there in the room?"""
    # calculate the total legs of the tables, sofa and chairs
    total_tables = 4 + 3 + 1
    legs_per_table = 4
    total_table_legs = total_tables * legs_per_table
    
    total_sofa_legs = 0 # sofa has no legs
    
    total_chairs = 2
    legs_per_chair = 4
    total_chair_legs = total_chairs * legs_per_chair
    
    # calculate the total legs of the tables with 3 legs each, one table with 1 leg and one rocking chair with 2 legs
    total_three_legged_tables = 3
    legs_per_three_legged_table = 3
    total_three_legged_table_legs = total_three_legged_tables * legs_per_three_legged_table
    
    total_one_legged_table_legs = 1
    
    total_rocking_chair_legs = 2
    
    # calculate the total number of legs in the room
    total_legs = (total_table_legs + total_sofa_legs + total_chair_legs +
                  total_three_legged_table_legs + total_one_legged_table_legs + total_rocking_chair_legs)
    
    result = total_legs
    return result

print(solution())