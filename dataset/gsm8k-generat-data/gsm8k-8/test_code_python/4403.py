def solution():
    # Define some variables
    manny = 1
    aaron = 0
    kai = 2 * manny
    raphael = 0.5 * manny
    lisa = 2 + raphael
    
    # Calculate the total needed pieces
    total_pieces = manny + aaron + kai + raphael + lisa
    
    # Round up to the nearest whole number
    total_pieces = math.ceil(total_pieces)
    
    result = total_pieces
    return result

print(solution())