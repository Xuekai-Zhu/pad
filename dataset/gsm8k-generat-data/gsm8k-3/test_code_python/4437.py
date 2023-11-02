def solution():
    """Giselle is in charge of the relay run on track and field day. Last year, the race was 300 meters. This year, it will be 4 times as long. Giselle needs to set up 6 tables for the relay run. The distance between the tables must be the same and the last table will be at the finish line. What is the distance between table 1 and table 3 in meters?"""
    # Define the length of the race this year and the number of tables
    RACE_LENGTH = 1200
    NUM_TABLES = 6

    # Calculate the distance between each table
    table_distance = RACE_LENGTH / (NUM_TABLES - 1)

    # Calculate the distance between table 1 and table 3
    distance_1_3 = 2 * table_distance

    # Display the distance between table 1 and table 3
    result = distance_1_3
    return result

print(solution())