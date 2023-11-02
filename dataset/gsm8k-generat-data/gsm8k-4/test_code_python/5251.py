def solution():
    """Donna made a cake to take to a party where the guests ate half the cake. The day after the party, she shared half the leftovers with her brothers. The following day, she ate one piece as a midnight snack. Twice as many pieces as her snack were left. How many pieces was the cake to begin with?"""
    # Define the initial number of cake pieces
    cake_pieces = None

    # Calculate the number of cake pieces left after the party
    cake_pieces = cake_pieces / 2

    # Calculate the number of cake pieces left after sharing with her brothers
    cake_pieces = cake_pieces / 2

    # Calculate the number of cake pieces left after Donna's midnight snack
    cake_pieces -= 1

    # Calculate the number of cake pieces left after twice as many as Donna's snack
    cake_pieces = cake_pieces * 2

    # display the result
    result = cake_pieces
    return result

print(solution())