def solution():
    total_pieces = 1000

    # Calculate the number of pieces Luke put together on the first day
    day_1_pieces = total_pieces * 0.1

    # Calculate the number of pieces remaining after the first day
    remaining_pieces = total_pieces - day_1_pieces

    # Calculate the number of pieces Luke put together on the second day
    day_2_pieces = remaining_pieces * 0.2

    # Calculate the number of pieces remaining after the second day
    remaining_pieces = remaining_pieces - day_2_pieces

    # Calculate the number of pieces Luke put together on the third day
    day_3_pieces = remaining_pieces * 0.3

    # Calculate the number of pieces remaining after the third day
    remaining_pieces = remaining_pieces - day_3_pieces

    result = remaining_pieces
    return result

print(solution())