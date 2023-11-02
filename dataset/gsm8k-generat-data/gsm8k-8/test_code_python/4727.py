def solution():
    # Determine how many minutes after March 1st it is currently
    current_days = 40
    current_minutes = 10
    minutes_since_march1 = (current_days * 24 * 60) + (current_minutes)

    # Calculate how many minutes after March 1st the sun sets on March 2nd
    minutes_per_day_increase = 1.2
    march2_minutes_since_march1 = 24 * 60
    march2_minutes_after_sunset = march2_minutes_since_march1 - (6 * 60)
    march2_minutes_after_first_sunset = march2_minutes_after_sunset + minutes_per_day_increase

    # Calculate how many minutes after March 1st the sun sets on the current day
    minutes_after_first_sunset = march2_minutes_after_first_sunset + (minutes_per_day_increase * (current_days - 1))

    # Calculate how many minutes until the sun sets on the current day
    minutes_in_a_day = 24 * 60
    minutes_until_sunset = minutes_in_a_day - (current_minutes + minutes_after_first_sunset)

    result = minutes_until_sunset
    return result

print(solution())