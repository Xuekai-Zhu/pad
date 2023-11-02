def solution():
    """Lucca bought 200 pieces of bread. Lucca ate 1/4 of the pieces of bread in one day, and 2/5 of the remaining pieces the next day. If he ate half of the remaining pieces on the third day, calculate how many pieces of bread are remaining."""
    # Define the initial number of pieces of bread
    initial_bread = 200

    # Calculate the number of pieces of bread Lucca ate on the first day
    day1_bread = initial_bread / 4

    # Calculate the remaining number of pieces of bread
    remaining_bread1 = initial_bread - day1_bread

    # Calculate the number of pieces of bread Lucca ate on the second day
    day2_bread = (2 / 5) * remaining_bread1

    # Calculate the remaining number of pieces of bread
    remaining_bread2 = remaining_bread1 - day2_bread

    # Calculate the number of pieces of bread Lucca ate on the third day
    day3_bread = remaining_bread2 / 2

    # Calculate the total number of pieces of bread remaining
    total_remaining_bread = remaining_bread2 - day3_bread

    # return the result
    result = total_remaining_bread
    return result

print(solution())