def solution():
    """Luke started working on a 1000-piece jigsaw puzzle. The first day he worked on it, he put together 10% of the pieces. On the second day, he put together another 20% of the remaining pieces from the first day. On the third day, he put together 30% of the remaining pieces from the previous day. How many pieces does he have left to complete after the third day?"""
    
    # Define the initial total number of pieces and the pieces completed each day
    total_pieces = 1000
    day1_pieces = total_pieces * 0.1
    day2_pieces = (total_pieces - day1_pieces) * 0.2
    day3_pieces = (total_pieces - day1_pieces - day2_pieces) * 0.3

    # Calculate the pieces left to complete after the third day
    pieces_left = total_pieces - day1_pieces - day2_pieces - day3_pieces

    result = pieces_left
    return result

print(solution())