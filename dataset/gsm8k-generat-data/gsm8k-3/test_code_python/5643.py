def solution():
    """Aron spends 30 minutes/day three times a week vacuuming and 20 minutes/day 2 days a week dusting. How much time does he spend cleaning total each week?"""
    # Define the time spent vacuuming and dusting per day and per week
    VACUUM_TIME_PER_DAY = 30
    VACUUM_DAYS_PER_WEEK = 3
    DUSTING_TIME_PER_DAY = 20
    DUSTING_DAYS_PER_WEEK = 2

    # Calculate the total time spent vacuuming per week
    vacuum_time_per_week = VACUUM_TIME_PER_DAY * VACUUM_DAYS_PER_WEEK

    # Calculate the total time spent dusting per week
    dusting_time_per_week = DUSTING_TIME_PER_DAY * DUSTING_DAYS_PER_WEEK

    # Calculate the total time spent cleaning per week
    total_time_per_week = vacuum_time_per_week + dusting_time_per_week

    # Display the total time spent cleaning 
    result = total_time_per_week
    return result

print(solution())