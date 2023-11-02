def solution():
    """James spends 30 minutes twice a day on meditation. How many hours a week does he spend meditating?"""
    # Define the time spent on meditation per day and the number of days in a week
    meditation_per_day = 30/60 # Convert 30 minutes to hours
    days_in_week = 7

    # Calculate the total time spent on meditation in a week
    meditation_per_week = 2 * meditation_per_day * days_in_week

    # Return the result
    result = meditation_per_week
    return result

print(solution())