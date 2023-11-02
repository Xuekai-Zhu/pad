def solution():
    """Luke started working on a 1000-piece jigsaw puzzle. The first day he worked on it, he put together 10% of the pieces. On the second day, he put together another 20% of the remaining pieces from the first day. On the third day, he put together 30% of the remaining pieces from the previous day. How many pieces does he have left to complete after the third day?"""
    # Define the number of puzzle pieces
    num_pieces = 1000

    # Calculate the number of pieces Luke put together on the first day
    pieces_day1 = num_pieces * 0.1

    # Calculate the number of pieces remaining after the first day
    pieces_remaining_day1 = num_pieces - pieces_day1

    # Calculate the number of pieces Luke put together on the second day
    pieces_day2 = pieces_remaining_day1 * 0.2

    # Calculate the number of pieces remaining after the second day
    pieces_remaining_day2 = pieces_remaining_day1 - pieces_day2

    # Calculate the number of pieces Luke put together on the third day
    pieces_day3 = pieces_remaining_day2 * 0.3

    # Calculate the number of pieces remaining after the third day
    pieces_remaining_day3 = pieces_remaining_day2 - pieces_day3

    # Display the number of pieces remaining after the third day
    result = pieces_remaining_day3
    return result

print(solution())