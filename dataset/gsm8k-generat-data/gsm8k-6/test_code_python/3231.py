def solution():
    # Calculate the number of pieces of bread Lucca ate in one day
    pieces_eaten_day1 = 1/4 * 200

    # Calculate the number of pieces of bread remaining after day 1
    pieces_remaining_day1 = 200 - pieces_eaten_day1

    # Calculate the number of pieces of bread Lucca ate on day 2
    pieces_eaten_day2 = 2/5 * pieces_remaining_day1

    # Calculate the number of pieces of bread remaining after day 2
    pieces_remaining_day2 = pieces_remaining_day1 - pieces_eaten_day2

    # Calculate the number of pieces of bread Lucca ate on day 3
    pieces_eaten_day3 = 1/2 * pieces_remaining_day2

    # Calculate the number of pieces of bread remaining after day 3
    pieces_remaining_day3 = pieces_remaining_day2 - pieces_eaten_day3

    result = pieces_remaining_day3
    return result

print(solution())