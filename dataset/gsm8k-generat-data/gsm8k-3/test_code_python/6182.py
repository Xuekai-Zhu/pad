def solution():
    """Alan counted how many chairs the office canteen has. It has 2 round tables and 2 rectangular tables. Each round table has 6 chairs, and each rectangular table has 7 chairs. How many chairs are there in all?"""
    # Define the number of chairs per round table and rectangular table
    ROUND_CHAIRS = 6
    RECTANGLE_CHAIRS = 7

    # Define the number of tables of each type
    ROUND_TABLES = 2
    RECTANGLE_TABLES = 2

    # Calculate the total number of chairs
    total_chairs = (ROUND_TABLES * ROUND_CHAIRS) + (RECTANGLE_TABLES * RECTANGLE_CHAIRS)

    # Display the total number of chairs
    result = total_chairs
    return result

print(solution())