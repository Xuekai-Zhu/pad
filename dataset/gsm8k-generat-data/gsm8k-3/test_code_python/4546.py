def solution():
    """Gerald is a furniture maker. He has 672 pieces of wood and he wants to make some tables and chairs. It takes 12 pieces of wood to make a table and 8 pieces of wood to make a chair. How many chairs can he make if he makes 24 tables?"""
    # Define the number of pieces of wood needed for a table and a chair
    TABLE_WOOD = 12
    CHAIR_WOOD = 8

    # Define the number of tables Gerald wants to make
    num_tables = 24

    # Calculate the total number of pieces of wood needed for the tables
    table_wood = num_tables * TABLE_WOOD

    # Calculate the remaining pieces of wood available for making chairs
    remaining_wood = 672 - table_wood

    # Calculate the maximum number of chairs Gerald can make
    max_chairs = remaining_wood // CHAIR_WOOD

    # Display the maximum number of chairs Gerald can make
    result = max_chairs
    return result

print(solution())