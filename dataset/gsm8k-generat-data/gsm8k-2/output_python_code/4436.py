def solution():
    """Giselle is in charge of the relay run on track and field day. Last year, the race was 300 meters. This year, it will be 4 times as long. Giselle needs to set up 6 tables for the relay run. The distance between the tables must be the same and the last table will be at the finish line. What is the distance between table 1 and table 3 in meters?"""
    last_year_distance = 300
    this_year_distance = last_year_distance * 4
    table_count = 6
    distance_between_tables = this_year_distance / (table_count - 1)
    distance_between_table_1_and_3 = distance_between_tables * 2
    result = distance_between_table_1_and_3
    return result

print(solution())