def solution():
    num_pieces = 100
    piece_length = 15  # in centimeters

    total_length = num_pieces * piece_length / 100  # convert to meters

    ribbon_length = 51  # in meters

    remaining_length = ribbon_length - total_length
    result = remaining_length
    return result

print(solution())