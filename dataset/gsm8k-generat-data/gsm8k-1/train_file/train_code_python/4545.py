def solution():
    """Gerald is a furniture maker. He has 672 pieces of wood and he wants to make some tables and chairs. It takes 12 pieces of wood to make a table and 8 pieces of wood to make a chair. How many chairs can he make if he makes 24 tables?"""
    pieces_of_wood = 672
    pieces_per_table = 12
    pieces_per_chair = 8
    total_pieces_for_tables = pieces_per_table * 24
    pieces_left = pieces_of_wood - total_pieces_for_tables
    chairs = pieces_left // pieces_per_chair
    result = chairs
    
    return result

print(solution())