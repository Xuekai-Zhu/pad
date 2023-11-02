def solution():
    """There were 349 pieces of candy in a bowl. Talitha took 108 pieces and Solomon took 153 pieces. How many pieces of candy remain in the bowl?"""
    # Define the initial number of candy pieces
    initial_pieces = 349

    # Define the number of candy pieces taken by Talitha
    talitha_pieces = 108

    # Define the number of candy pieces taken by Solomon
    solomon_pieces = 153

    # Calculate the remaining number of candy pieces
    remaining_pieces = initial_pieces - talitha_pieces - solomon_pieces

    # return the result
    result = remaining_pieces
    return result

print(solution())