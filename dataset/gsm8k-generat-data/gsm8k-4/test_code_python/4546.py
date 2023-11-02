def solution():
    """Gerald is a furniture maker. He has 672 pieces of wood and he wants to make some tables and chairs. It takes 12 pieces of wood to make a table and 8 pieces of wood to make a chair. How many chairs can he make if he makes 24 tables?"""
    # Define the number of pieces of wood needed to make a table and a chair
    TABLE_WOOD = 12
    CHAIR_WOOD = 8

    # Define the number of pieces of wood Gerald has
    wood_available = 672

    # Calculate the number of pieces of wood needed to make 24 tables
    table_wood_needed = 24 * TABLE_WOOD

    # Calculate the remaining pieces of wood after making the tables
    remaining_wood = wood_available - table_wood_needed

    # Calculate the number of chairs Gerald can make with the remaining wood
    chairs_made = remaining_wood // CHAIR_WOOD

    result = chairs_made
    return result

print(solution())