def solution():
    total_pieces = 1000  # Luke starts with a 1000-piece puzzle
    pieces_completed = total_pieces * 0.1  # Luke completes 10% of the puzzle on the first day
    pieces_remaining = total_pieces - pieces_completed  # Luke has some pieces left to complete on the second day

    # Luke completes 20% of the remaining pieces on second day
    pieces_completed += pieces_remaining * 0.2
    pieces_remaining = total_pieces - pieces_completed  # Luke has some pieces left to complete on the third day

    # Luke completes 30% of the remaining pieces on third day
    pieces_completed += pieces_remaining * 0.3
    pieces_remaining = total_pieces - pieces_completed  # Luke has these many pieces left to complete after three days
    result = pieces_remaining
    return result

print(solution())