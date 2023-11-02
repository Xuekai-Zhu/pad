def solution():
    """Gerald is a furniture maker. He has 672 pieces of wood and he wants to make some tables and chairs. It takes 12 pieces of wood to make a table and 8 pieces of wood to make a chair. How many chairs can he make if he makes 24 tables?"""
    total_wood = 672
    table_wood = 12
    chair_wood = 8

    # Calculate the total wood used for 24 tables
    table_wood_use = table_wood * 24

    # Calculate the remaining wood after making the tables
    remaining_wood = total_wood - table_wood_use

    # Calculate the number of chairs that can be made with the remaining wood
    chair_count = remaining_wood // chair_wood

    result = chair_count
    return result

print(solution())