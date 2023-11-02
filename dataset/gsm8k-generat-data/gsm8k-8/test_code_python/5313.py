def solution():
    # Calculate the number of cake pieces left after 60% were eaten
    remaining_pieces = 0.4 * 240

    # Divide the remaining pieces equally among Juelz's three sisters
    pieces_per_sister = remaining_pieces / 3

    result = pieces_per_sister
    return result

print(solution())