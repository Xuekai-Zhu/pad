def solution():
    """A cafe has 9 indoor tables and 11 outdoor tables. Each indoor table has 10 chairs, and each outdoor table has 3 chairs. How many chairs are there in all?"""
    # Define the number of indoor and outdoor tables
    indoor_tables = 9
    outdoor_tables = 11

    # Define the number of chairs per indoor and outdoor table
    indoor_chairs = 10
    outdoor_chairs = 3

    # Calculate the total number of chairs
    total_chairs = indoor_tables * indoor_chairs + outdoor_tables * outdoor_chairs

    # Display the total number of chairs
    result = total_chairs
    return result

print(solution())