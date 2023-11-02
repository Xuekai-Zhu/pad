def solution():
    # Calculate the total number of matches Jimmy has
    total_matches = 5 * 24  # Jimmy has 5 matchbooks, each with 24 matches

    # Calculate the total number of stamps Tonya and Jimmy trade
    traded_stamps = total_matches / 12  # One stamp is worth 12 matches

    # Calculate the number of stamps Tonya has left after the trade
    remaining_stamps = 13 - traded_stamps  # Tonya starts with 13 stamps

    result = remaining_stamps
    return result

print(solution())