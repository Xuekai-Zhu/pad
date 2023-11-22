def solution():
    
    # Define the total number of pizza pieces
    total_pieces = 60

    # Calculate the number of pieces eaten on the first day
    day1_pieces = total_pieces * (2/5)

    # Calculate the number of pieces remaining after the first day
    remaining_pieces = total_pieces - day1_pieces

    # Calculate the number of pieces eaten on the second day
    day2_pieces = remaining_pieces * 10

    # Calculate the number of pieces remaining after the second day
    remaining_pieces = remaining_pieces - day2_pieces

    # Calculate the number of pieces eaten on the third day
    day3_pieces = remaining_pieces * (7/13)

    # Calculate the total number of pieces eaten
    total_pieces_eaten = day1_pieces + day2_pieces + day3_pieces

    # Display the total number of pieces eaten
    result = total_pieces_eaten
    return result

print(solution())