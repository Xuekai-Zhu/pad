def solution():
    """Forest and his friends have prepared a birthday cake for their friend Juelz having 240 cake pieces. After singing the birthday song, they ate 60% of the cake's pieces, and later, Juelz divided the remaining pieces among his three sisters. What is the number of pieces of cake each sister received?"""
    # Define the initial number of cake pieces
    initial_pieces = 240

    # Calculate the number of pieces left after 60% were eaten
    remaining_pieces = initial_pieces * (1 - 0.6)

    # Calculate the number of pieces each sister received
    pieces_per_sister = remaining_pieces / 3

    # Round the result to the nearest whole number
    result = round(pieces_per_sister)
    return result

print(solution())