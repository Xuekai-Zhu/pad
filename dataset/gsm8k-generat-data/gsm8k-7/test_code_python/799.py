def solution():
    # Calculate the total number of legs for the tables (4 tables with 4 legs each, 3 tables with 3 legs each, and 1 table with 1 leg)
    total_table_legs = (4 * 4) + (3 * 3) + 1

    # Calculate the total number of legs for the chairs (2 chairs with 4 legs each and 1 rocking chair with 2 legs)
    total_chair_legs = (2 * 4) + 2

    # Add up the total number of legs in the room
    total_legs = total_table_legs + total_chair_legs
    result = total_legs
    return result

print(solution())