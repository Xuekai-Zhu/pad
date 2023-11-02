def solution():
    hours_per_day = 2  # Jordan plays video games for 2 hours every day
    part_time_job = 10  # Jordan earns $10 an hour
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of hours Jordan played in a week
    total_hours = hours_per_day * days_per_week

    # Calculate the total amount Jordan earns in a week
    total_earnings = total_hours * part_time_job
    result = total_earnings
    return result

print(solution())