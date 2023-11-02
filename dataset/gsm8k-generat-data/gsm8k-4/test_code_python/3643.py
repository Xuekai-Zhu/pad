def solution():
    """The bakery has 8 indoor tables and 12 outdoor tables. Each indoor table has 3 chairs and each outdoor table has 3 chairs. How many chairs are there in total?"""
    # Define the number of indoor and outdoor tables
    indoor_tables = 8
    outdoor_tables = 12

    # Define the number of chairs per table
    chairs_per_table = 3

    # Calculate the total number of chairs
    total_chairs = (indoor_tables * chairs_per_table) + (outdoor_tables * chairs_per_table)

    # return the result
    result = total_chairs
    return result

print(solution())