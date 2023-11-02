def solution():
    """There are 32 tables in a hall. Half the tables have 2 chairs each, 5 have 3 chairs each and the rest have 4 chairs each. How many chairs in total are in the hall?"""
    # Define the number of tables and chairs
    NUM_TABLES = 32
    HALF_NUM_TABLES = NUM_TABLES // 2
    NUM_3_CHAIR_TABLES = 5

    # Calculate the total number of chairs
    total_chairs = HALF_NUM_TABLES * 2 + NUM_3_CHAIR_TABLES * 3 + (NUM_TABLES - HALF_NUM_TABLES - NUM_3_CHAIR_TABLES) * 4

    # Display the total number of chairs
    result = total_chairs
    return result

print(solution())