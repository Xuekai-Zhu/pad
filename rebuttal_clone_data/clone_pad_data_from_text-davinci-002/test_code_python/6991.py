def solution():
    pieces = 1000
    day_one = pieces * 0.10
    day_two = pieces * 0.20
    day_three = pieces * 0.30
    total_pieces = day_one + day_two + day_three
    pieces_left = pieces - total_pieces
    result = pieces_left
    return result

print(solution())