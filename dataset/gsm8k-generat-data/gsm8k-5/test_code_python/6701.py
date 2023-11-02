def solution():
    sleep_sun_to_thurs = 6 * 5  # Prudence sleeps 6 hours a night from Sunday to Thursday
    sleep_fri_and_sat = 9 * 2  # Prudence sleeps 9 hours a night on Friday and Saturday
    nap_time = 1 * 2  # Prudence takes a 1-hour nap on Saturday and Sunday
    total_sleep_per_week = sleep_sun_to_thurs + sleep_fri_and_sat + nap_time  # Calculate the total sleep each week
    total_sleep_4_weeks = total_sleep_per_week * 4  # Multiply the sleep per week by the number of weeks
    result = total_sleep_4_weeks
    return result

print(solution())