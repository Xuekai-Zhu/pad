def solution():
    total_hours = 4 * 14  # John played 4 hours for 14 days
    progress = 0.4  # John was only 40% done after playing for 4 hours a day for 2 weeks
    remaining_progress = 1 - progress  # John needs to complete the remaining 60% of the game
    hours_needed_at_4_hours_per_day = (remaining_progress / progress) * total_hours  # Calculate the total hours needed to complete the game at a rate of 4 hours per day
    hours_needed_at_7_hours_per_day = hours_needed_at_4_hours_per_day / 7  # Calculate the hours needed to complete the game at a rate of 7 hours per day

    result = hours_needed_at_7_hours_per_day
    return result

print(solution())