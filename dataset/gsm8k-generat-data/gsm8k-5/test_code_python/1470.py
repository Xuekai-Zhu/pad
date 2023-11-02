def solution():
    jog_time_per_day = 0.5  # Ayen jogs for 30 minutes or 0.5 hours every weekday
    extra_jog_time_on_tuesday = 5 / 60  # Ayen jogged for 5 minutes extra on Tuesday
    extra_jog_time_on_friday = 25 / 60  # Ayen jogged for 25 minutes extra on Friday
    total_jog_time = (4 * jog_time_per_day) + extra_jog_time_on_tuesday + extra_jog_time_on_friday

    result = total_jog_time
    return result

print(solution())