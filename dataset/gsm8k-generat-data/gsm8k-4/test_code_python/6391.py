def solution():
    """Trevor and Joe were working together to finish a 500 piece puzzle.  They put the border together first and that was 75 pieces.  Trevor was able to place 105 pieces of the puzzle.  Joe was able to place three times the number of puzzle pieces as Trevor.  How many puzzle pieces are missing?"""
    # Define the number of puzzle pieces
    total_pieces = 500

    # Define the number of border pieces
    border_pieces = 75

    # Define the number of pieces placed by Trevor
    trevor_pieces = 105

    # Calculate the number of pieces placed by Joe
    joe_pieces = 3 * trevor_pieces

    # Calculate the total number of pieces placed
    total_placed = border_pieces + trevor_pieces + joe_pieces

    # Calculate the number of missing pieces
    missing_pieces = total_pieces - total_placed

    # return the result
    result = missing_pieces
    return result

print(solution())