def solution():
    # Calculate the total number of stamps Marie has
    total_stamps = 4 * 20 + 2 * 50  # 4 notebooks with 20 stamps each and 2 binders with 50 stamps each
    # Calculate the number of stamps Marie keeps
    kept_stamps = total_stamps / 4
    # Calculate the number of stamps Marie can give away
    given_away_stamps = total_stamps - kept_stamps
    result = given_away_stamps
    return result

print(solution())