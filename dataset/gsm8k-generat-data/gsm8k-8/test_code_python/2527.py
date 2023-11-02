def solution():
    # Define the number of indoor and outdoor tables and the number of chairs per table
    indoor_tables = 9
    outdoor_tables = 11
    indoor_chairs_per_table = 10
    outdoor_chairs_per_table = 3

    # Calculate the total number of chairs in all tables
    total_chairs = (indoor_tables * indoor_chairs_per_table) + (outdoor_tables * outdoor_chairs_per_table)
    result = total_chairs
    return result

print(solution())