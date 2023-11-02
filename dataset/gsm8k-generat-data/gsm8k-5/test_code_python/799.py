def solution():
    # Calculate total number of legs on tables with 4 legs each
    legs_4_legged_tables = 4 * 4

    # Calculate total number of legs on tables with 3 legs each
    legs_3_legged_tables = 3 * 3

    # Calculate total number of legs on table with 1 leg
    legs_1_legged_table = 1

    # Calculate total number of legs on rocking chair with 2 legs
    legs_rocking_chair = 2

    # Calculate total number of legs in the room
    total_legs = legs_4_legged_tables + legs_3_legged_tables + legs_1_legged_table + legs_rocking_chair

    result = total_legs
    return result

print(solution())