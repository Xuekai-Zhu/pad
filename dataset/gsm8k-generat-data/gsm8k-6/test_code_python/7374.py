def solution():
    # Calculate the total number of pies left after selling and giving away
    total_pies = 4 - 1 - 1  # 4 whole pies minus 1 sold and 1 given away
    # Calculate the total number of pieces of pumpkin pie
    total_pieces = total_pies * 6  # Each remaining whole pie is sliced into 6 pieces
    # Calculate the number of pieces eaten by Grace's family
    pieces_eaten = total_pieces * (2/3)
    # Calculate the number of pieces of pumpkin pie left
    pieces_left = total_pieces - pieces_eaten
    result = pieces_left
    return result

print(solution())