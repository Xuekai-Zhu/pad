def solution():
    """A cafe has 9 indoor tables and 11 outdoor tables. Each indoor table has 10 chairs, and each outdoor table has 3 chairs. How many chairs are there in all?"""
    indoor_tables = 9
    outdoor_tables = 11
    indoor_chairs_per_table = 10
    outdoor_chairs_per_table = 3
    total_indoor_chairs = indoor_tables * indoor_chairs_per_table
    total_outdoor_chairs = outdoor_tables * outdoor_chairs_per_table
    total_chairs = total_indoor_chairs + total_outdoor_chairs
    result = total_chairs
    return result

print(solution())