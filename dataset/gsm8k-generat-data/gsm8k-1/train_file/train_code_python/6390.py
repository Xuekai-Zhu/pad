def solution():
    """Trevor and Joe were working together to finish a 500 piece puzzle. They put the border together first and that was 75 pieces. Trevor was able to place 105 pieces of the puzzle. Joe was able to place three times the number of puzzle pieces as Trevor. How many puzzle pieces are missing?"""
    total_pieces = 500
    border_pieces = 75
    trevor_pieces = 105
    joe_pieces = trevor_pieces * 3
    placed_pieces = border_pieces + trevor_pieces + joe_pieces
    missing_pieces = total_pieces - placed_pieces
    result = missing_pieces
    return result

print(solution())