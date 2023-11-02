def solution():
    """There is a very large room that has 4 tables, 1 sofa and 2 chairs that have 4 legs each. There are also 3 tables with 3 legs each, 1 table
    with 1 leg, and 1 rocking chair with 2 legs. How many legs are there in the room?"""
    
    # Define the number of legs for each piece of furniture
    table_legs = 4
    sofa_legs = 0 # no information given about sofa legs
    chair_legs = 4
    three_legged_table_legs = 3
    one_legged_table_legs = 1
    rocking_chair_legs = 2

    # Calculate the total number of legs for each type of furniture
    total_table_legs = 4 * table_legs + 3 * three_legged_table_legs + one_legged_table_legs
    total_sofa_legs = sofa_legs
    total_chair_legs = 2 * chair_legs + rocking_chair_legs

    # Calculate the total number of legs in the room
    total_legs = total_table_legs + total_sofa_legs + total_chair_legs

    # return the result
    result = total_legs
    return result

print(solution())