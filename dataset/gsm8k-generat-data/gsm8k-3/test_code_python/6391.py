def solution():
    """Trevor and Joe were working together to finish a 500 piece puzzle.  They put the border together first and that was 75 pieces.  Trevor was able to place 105 pieces of the puzzle.  Joe was able to place three times the number of puzzle pieces as Trevor.  How many puzzle pieces are missing?"""
    # Define the number of puzzle pieces in the puzzle and the border
    TOTAL_PIECES = 500
    BORDER_PIECES = 75

    # Calculate the number of puzzle pieces placed by Trevor
    trevor_pieces = 105

    # Calculate the number of puzzle pieces placed by Joe
    joe_pieces = trevor_pieces * 3

    # Calculate the total number of puzzle pieces placed
    total_pieces = BORDER_PIECES + trevor_pieces + joe_pieces

    # Calculate the number of puzzle pieces missing
    missing_pieces = TOTAL_PIECES - total_pieces

    # Display the number of puzzle pieces missing
    result = missing_pieces
    
    return result

print(solution())