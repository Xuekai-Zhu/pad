def solution():
    """Jade is building a lego tower. She has 100 pieces. Each level has to be 7 pieces wide. If she has 23 pieces left at the end, how many levels is her tower?"""
    # Define the total number of lego pieces and pieces per level
    total_pieces = 100
    pieces_per_level = 7

    # Calculate the number of levels
    levels = (total_pieces - 23) // pieces_per_level

    # return the result
    result = levels
    return result

print(solution())