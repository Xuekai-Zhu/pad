def solution():
    # Calculate her initial daily reading
    initial_daily_reading = 3 * 6

    # Calculate her total initial weekly reading
    initial_weekly_reading = initial_daily_reading * 7

    # Calculate the difference between her initial weekly reading and her goal
    difference = 140 - initial_weekly_reading

    # Calculate how many more pages she needs to read per day to reach her goal
    more_per_day = difference / 7

    result = more_per_day
    return result

print(solution())