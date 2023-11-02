def solution():
    num_indoor_tables = 9
    num_outdoor_tables = 11

    num_chairs_per_indoor_table = 10
    num_chairs_per_outdoor_table = 3

    # Calculate the total number of chairs in all indoor tables
    total_chairs_indoor = num_indoor_tables * num_chairs_per_indoor_table

    # Calculate the total number of chairs in all outdoor tables
    total_chairs_outdoor = num_outdoor_tables * num_chairs_per_outdoor_table

    # Calculate the total number of chairs in all tables
    total_chairs = total_chairs_indoor + total_chairs_outdoor
    result = total_chairs
    return result

print(solution())