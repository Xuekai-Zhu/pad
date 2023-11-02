def solution():
    """A bar of chocolate is made up of 60 pieces. If Michael takes half of the bar, Paige takes half of the remainder, and Mandy is left with what’s left of the chocolate bar, how many pieces of chocolate will Mandy get?"""
    chocolate_pieces = 60
    michael = chocolate_pieces // 2
    paige = (chocolate_pieces - michael) // 2
    mandy = chocolate_pieces - michael - paige
    result = mandy
    return result

print(solution())