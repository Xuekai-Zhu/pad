def solution():
    num_pieces = 12
    eaten_fraction = 1/4   # one-fourth of the cake was eaten

    # Calculate the number of pieces eaten by the visitors
    num_eaten = num_pieces * eaten_fraction

    # Calculate the number of pieces left
    num_left = num_pieces - num_eaten
    result = num_left
    return result

print(solution())