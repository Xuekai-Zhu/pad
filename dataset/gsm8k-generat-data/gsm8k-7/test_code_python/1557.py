def solution():
    max_tan_minutes = 200
    daily_tan_minutes = 30
    first_two_weeks_tan_minutes = 2 * 2 * daily_tan_minutes

    # Calculate how many minutes Jenna tanned in the first two weeks and subtract it from the maximum allowed
    remaining_tan_minutes = max_tan_minutes - first_two_weeks_tan_minutes

    # Calculate how many minutes Jenna can tan per day in the last two weeks to stay under the maximum allowed
    remaining_days = 14 - (2 * 2)
    max_daily_tan_minutes = remaining_tan_minutes / remaining_days
    result = max_daily_tan_minutes
    return result

print(solution())