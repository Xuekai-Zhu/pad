def solution():
    """Before work, Hayden spends 5 minutes ironing his button-up shirt and 3 minutes ironing his pants.  He does this 5 days a week.  How many minutes does he iron over 4 weeks?"""
    # Define the time in minutes Hayden spends ironing each day
    SHIRT_IRONING_TIME = 5
    PANTS_IRONING_TIME = 3

    # Define the number of days per week Hayden irons
    IRONING_DAYS_PER_WEEK = 5

    # Define the number of weeks being considered
    WEEKS = 4

    # Calculate the total time Hayden spends ironing over 4 weeks
    total_time = (SHIRT_IRONING_TIME + PANTS_IRONING_TIME) * IRONING_DAYS_PER_WEEK * WEEKS

    # Display the total time
    result = total_time
    return result

print(solution())