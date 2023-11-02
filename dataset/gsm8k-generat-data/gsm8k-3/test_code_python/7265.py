def solution():
    """A bar of chocolate is made up of 60 pieces. If Michael takes half of the bar, Paige takes half of the remainder, and Mandy is left with what’s left of the chocolate bar, how many pieces of chocolate will Mandy get?"""
    # Define the number of pieces in the chocolate bar
    TOTAL_PIECES = 60

    # Calculate the number of pieces Michael takes
    michael_pieces = TOTAL_PIECES // 2

    # Calculate the number of pieces Paige takes
    paige_pieces = (TOTAL_PIECES - michael_pieces) // 2

    # Calculate the number of pieces Mandy gets
    mandy_pieces = TOTAL_PIECES - michael_pieces - paige_pieces

    # Display the number of pieces Mandy gets
    result = mandy_pieces
    return result

print(solution())