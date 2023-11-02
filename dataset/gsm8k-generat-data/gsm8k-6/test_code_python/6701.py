def solution():
    # Calculate the total number of hours slept by Prudence in a week
    weekly_hours = 5 * 6 + 2 * 9 + 2 * 1  # Sunday to Thursday she sleeps 6 hours a night, Friday and Saturday she sleeps for 9 hours a night, and she takes a 1-hour nap on Saturday and Sunday

    # Calculate the total number of hours slept by Prudence in 4 weeks
    total_hours = weekly_hours * 4

    result = total_hours
    return result

print(solution())