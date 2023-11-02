def solution():
    num_indoor_tables = 8
    num_outdoor_tables = 12
    chairs_per_table = 3

    # Calculate the total number of indoor chairs
    total_indoor_chairs = num_indoor_tables * chairs_per_table

    # Calculate the total number of outdoor chairs
    total_outdoor_chairs = num_outdoor_tables * chairs_per_table

    # Calculate the total number of chairs
    total_chairs = total_indoor_chairs + total_outdoor_chairs
    result = total_chairs
    return result

print(solution())