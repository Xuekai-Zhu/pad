def solution():
    # Calculate the total number of stamps Marie has
    total_stamps = (4 * 20) + (2 * 50)

    # Calculate the number of stamps Marie wants to keep
    kept_stamps = total_stamps / 4

    # Calculate the number of stamps Marie can give away
    given_away_stamps = total_stamps - kept_stamps
    result = given_away_stamps
    return result

print(solution())