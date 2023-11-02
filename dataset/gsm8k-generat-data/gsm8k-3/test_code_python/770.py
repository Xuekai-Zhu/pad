def solution():
    """
    Based on a 2008 study, children 6–11 years old spend 45 minutes each day watching television. How many hours do
    these children watch television in 2 weeks if they are allowed to watch television 4 days a week?
    """
    # Define the number of minutes per day children watch TV
    MINUTES_PER_DAY = 45

    # Define the number of days children are allowed to watch TV per week
    DAYS_PER_WEEK = 4

    # Define the number of weeks being considered
    WEEKS = 2

    # Calculate the total number of hours children watch TV
    hours_watched = (MINUTES_PER_DAY * DAYS_PER_WEEK * WEEKS) / 60

    # Display the total number of hours
    result = hours_watched
    return result

print(solution())