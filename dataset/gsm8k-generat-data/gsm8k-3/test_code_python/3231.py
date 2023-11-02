def solution():
    """Lucca bought 200 pieces of bread. Lucca ate 1/4 of the pieces of bread in one day, and 2/5 of the remaining pieces the next day. If he ate half of the remaining pieces on the third day, calculate how many pieces of bread are remaining."""
    # Define the initial number of pieces of bread
    initial_pieces = 200

    # Calculate the number of pieces of bread Lucca ate on the first day
    day1_eaten = initial_pieces / 4

    # Calculate the number of pieces of bread remaining after the first day
    day1_remaining = initial_pieces - day1_eaten

    # Calculate the number of pieces of bread Lucca ate on the second day
    day2_eaten = day1_remaining * (2 / 5)

    # Calculate the number of pieces of bread remaining after the second day
    day2_remaining = day1_remaining - day2_eaten

    # Calculate the number of pieces of bread Lucca ate on the third day
    day3_eaten = day2_remaining / 2

    # Calculate the number of pieces of bread remaining after the third day
    day3_remaining = day2_remaining - day3_eaten

    # Display the number of pieces of bread remaining
    result = day3_remaining
    return result

print(solution())