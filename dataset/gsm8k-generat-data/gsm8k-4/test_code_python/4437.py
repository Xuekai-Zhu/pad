def solution():
    """Giselle is in charge of the relay run on track and field day. Last year, the race was 300 meters. This year, it will be 4 times as long. Giselle needs to set up 6 tables for the relay run. The distance between the tables must be the same and the last table will be at the finish line. What is the distance between table 1 and table 3 in meters?"""
    # Define the total distance of the race
    total_distance = 300 * 4

    # Calculate the distance between each table (assuming equal distances)
    distance_between_tables = total_distance / (6 - 1)

    # Calculate the distance between table 1 and table 3
    distance_table_1_3 = distance_between_tables * 2

    # return the result
    result = distance_table_1_3
    return result

print(solution())