def solution():
    initial_number = 349  # There were 349 pieces of candy in a bowl
    talitha = 108  # Talitha took 108 pieces
    solomon = 153  # Solomon took 153 pieces

    # Calculate the remaining number of pieces
    remaining_pieces = initial_number - talitha - solomon
    result = remaining_pieces
    return result

print(solution())