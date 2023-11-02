def solution():
    """A bar of chocolate is made up of 60 pieces. If Michael takes half of the bar, Paige takes half of the remainder, and Mandy is left with what’s left of the chocolate bar, how many pieces of chocolate will Mandy get?"""
    total_pieces = 60
    michael_pieces = total_pieces // 2
    remainder1 = total_pieces - michael_pieces
    paige_pieces = remainder1 // 2
    remainder2 = remainder1 - paige_pieces
    mandy_pieces = remainder2
    result = mandy_pieces
    return result

print(solution())