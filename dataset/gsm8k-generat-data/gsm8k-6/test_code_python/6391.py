def solution():
    # Calculate the number of puzzle pieces placed by Joe
    joes_pieces = 3 * 105  # Joe was able to place three times the number of puzzle pieces as Trevor
    
    # Calculate the total number of puzzle pieces placed by Trevor and Joe
    total_pieces_placed = 75 + 105 + joes_pieces
    
    # Calculate the number of puzzle pieces missing
    missing_pieces = 500 - total_pieces_placed
    
    result = missing_pieces
    return result

print(solution())