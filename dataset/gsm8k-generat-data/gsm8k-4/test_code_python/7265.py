def solution():
    """A bar of chocolate is made up of 60 pieces. If Michael takes half of the bar, Paige takes half of the remainder, and Mandy is left with what’s left of the chocolate bar, how many pieces of chocolate will Mandy get?"""
    # Define the total number of pieces in the bar
    total_pieces = 60

    # Calculate the number of pieces taken by Michael
    michael_pieces = total_pieces / 2

    # Calculate the number of pieces remaining
    remaining_pieces = total_pieces - michael_pieces

    # Calculate the number of pieces taken by Paige
    paige_pieces = remaining_pieces / 2

    # Calculate the number of pieces left for Mandy
    mandy_pieces = remaining_pieces - paige_pieces

    # return the result
    result = mandy_pieces
    return result

print(solution())