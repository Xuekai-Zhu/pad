def solution():
    # Calculate the total number of matches Jimmy has
    total_matches = 5 * 24  # Jimmy has 5 matchbooks, and each matchbook contains 24 matches

    # Calculate the number of stamps Tonya will receive from Jimmy
    stamps_from_jimmy = total_matches / 12  # 1 stamp is worth 12 matches

    # Calculate the number of stamps Tonya has left after trading with Jimmy
    total_stamps = 13  # Tonya has 13 stamps
    stamps_left = total_stamps - stamps_from_jimmy

    result = stamps_left
    return result

print(solution())