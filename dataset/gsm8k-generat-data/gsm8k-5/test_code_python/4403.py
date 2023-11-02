def solution():
    number_of_friends = 4
    pieces_per_person = 1

    # Calculate the total number of pieces needed
    total_pieces = (number_of_friends - 1) * pieces_per_person  # Aaron doesn't want any

    # Calculate the number of pieces Lisa will have
    lisa_pieces = 2 + 0.5 * pieces_per_person  # Raphael will have half of Manny's, Lisa will have the rest

    # Calculate the number of pieces Kai will have
    kai_pieces = 2 * pieces_per_person  # Twice as much as Manny

    # Add Lisa's and Kai's pieces to the total
    total_pieces += lisa_pieces + kai_pieces
    result = total_pieces
    return result

print(solution())