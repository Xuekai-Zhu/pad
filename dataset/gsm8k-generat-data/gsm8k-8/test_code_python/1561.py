def solution():
    # Calculate the total number of stamps Marie has
    notebook_stamps = 4 * 20
    binder_stamps = 2 * 50
    total_stamps = notebook_stamps + binder_stamps

    # Calculate the number of stamps Marie wants to keep
    kept_stamps = total_stamps / 4

    # Calculate the number of stamps Marie can give away
    given_away_stamps = total_stamps - kept_stamps
    result = given_away_stamps
    return result

print(solution())