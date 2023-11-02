def solution():
    """Kimberly loves gumballs and will trade almost anything she owns for them. A friend knows that Kim has a bunch of shiny new earrings that she loves. She agrees to give Kim 9 gumballs for each pair of earrings. On the first day, Kim brings her 3 pairs of earrings. On the second she brings her twice as many. On the third day, she brings 1 less than she brought on the second day. If Kim eats 3 gumballs a day, how many days will the gumballs last?"""
    # Define the number of gumballs received for each pair of earrings
    GUMBALLS_PER_EARRING = 9

    # Calculate the number of pairs of earrings brought by Kim on each day
    earrings_day1 = 3
    earrings_day2 = 2 * earrings_day1
    earrings_day3 = earrings_day2 - 1

    # Calculate the total number of gumballs received by Kim
    total_gumballs = (earrings_day1 + earrings_day2 + earrings_day3) * GUMBALLS_PER_EARRING

    # Calculate the number of days the gumballs will last
    days = total_gumballs / 3

    # Display the number of days the gumballs will last
    result = days
    return result

print(solution())