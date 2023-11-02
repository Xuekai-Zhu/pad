def solution():
    """There is a very large room that has 4 tables, 1 sofa and 2 chairs that have 4 legs each.  There are also 3 tables with 3 legs each, 1 table with 1 leg, and 1 rocking chair with 2 legs.  How many legs are there in the room?"""
    # Define the number of legs for each item in the room
    TABLE_4_LEGS = 4
    SOFA_LEGS = 0 # Let's assume the sofa has no legs
    CHAIR_4_LEGS = 4
    TABLE_3_LEGS = 3
    TABLE_1_LEG = 1
    ROCKING_CHAIR_LEGS = 2

    # Calculate the total number of legs in the room
    total_legs = (4 * TABLE_4_LEGS) + (2 * CHAIR_4_LEGS) + (3 * TABLE_3_LEGS) + TABLE_1_LEG + ROCKING_CHAIR_LEGS

    # Display the total number of legs in the room
    result = total_legs
    return result

print(solution())