def solution():
    total_allowed_tanning_minutes = 200  # Jenna's doctor says she can tan no more than 200 minutes a month
    tanning_minutes_first_two_weeks = 30 * 2 * 2  # Jenna tans for 30 minutes a day, two days a week, for two weeks
    remaining_tanning_minutes = total_allowed_tanning_minutes - tanning_minutes_first_two_weeks  # Subtract the tanning minutes already used

    # Calculate the maximum number of tanning minutes Jenna can do in the last two weeks of the month
    max_tanning_minutes_last_two_weeks = remaining_tanning_minutes / 2
    result = max_tanning_minutes_last_two_weeks
    return result

print(solution())