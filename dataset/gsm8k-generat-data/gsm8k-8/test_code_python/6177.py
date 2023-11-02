def solution():
    # Define the initial number of brownie pieces
    initial_pieces = 16

    # Calculate the number of pieces eaten after school
    pieces_after_school = initial_pieces * 0.25

    # Calculate the number of pieces remaining after school
    remaining_pieces_1 = initial_pieces - pieces_after_school

    # Calculate the number of pieces eaten after dinner
    pieces_after_dinner = remaining_pieces_1 * 0.5

    # Calculate the number of pieces remaining after dinner
    remaining_pieces_2 = remaining_pieces_1 - pieces_after_dinner

    # Calculate the total number of brownies (pieces) left
    total_remaining_pieces = remaining_pieces_2 + 1

    result = total_remaining_pieces
    return result

print(solution())