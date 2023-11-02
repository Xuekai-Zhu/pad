def solution():
    """A cafe has 9 indoor tables and 11 outdoor tables. Each indoor table has 10 chairs, and each outdoor table has 3 chairs. How many chairs are there in all?"""
    # Define the number of indoor and outdoor tables
    indoor_tables = 9
    outdoor_tables = 11

    # Define the number of chairs per indoor and outdoor table
    chairs_per_indoor_table = 10
    chairs_per_outdoor_table = 3

    # Calculate the total number of chairs
    total_chairs = (indoor_tables * chairs_per_indoor_table) + (outdoor_tables * chairs_per_outdoor_table)

    # return the result
    result = total_chairs
    return result

print(solution())