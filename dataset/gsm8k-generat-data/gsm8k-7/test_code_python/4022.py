def solution():
    num_meditation_sessions_per_day = 2
    meditation_session_length_in_minutes = 30
    minutes_in_an_hour = 60
    days_in_a_week = 7

    # Calculate total minutes spent meditating per week
    total_minutes = num_meditation_sessions_per_day * meditation_session_length_in_minutes * days_in_a_week

    # Convert total minutes to hours
    total_hours = total_minutes / minutes_in_an_hour
    result = total_hours
    return result

print(solution())