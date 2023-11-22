def solution():
    
    # Define the time spent meditating and sleeping each day
    MEDITATION_TIME = 15 # minutes
    SLEEP_TIME = 15 # minutes

    # Define the number of days Charisma practices yoga per week
    DAYS_PER_WEEK = 5

    # Define the number of weeks Charisma practices yoga in 4 weeks
    WEEKS = 4

    # Calculate the total time spent meditation/sleeping
    total_time = (MEDITATION_TIME + SLEEP_TIME) * DAYS_PER_WEEK * WEEKS

    # Display the total time spent meditation/sleeping
    result = total_time
    return result

print(solution())